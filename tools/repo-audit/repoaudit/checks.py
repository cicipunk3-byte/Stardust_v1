"""Checks for repoaudit. Each returns a dict of findings.

Every check produces SIGNAL-class output. Nothing here is a verdict;
the runbook's human pass decides dispositions. Mark failures, do not
hide them: checks that cannot run report themselves as SKIPPED with a
reason.
"""

import fnmatch
import os
import re
import subprocess

# Markdown link target: ]( not http, not empty, may carry #fragment
_LINK_RE = re.compile(r"\]\((?!http)([^)#]+?)(#[^)]*)?\)")

_MARKERS = ("TODO", "FIXME", "XXX")


def _iter_md(root, skip_dirs=(".git", "node_modules", "__pycache__")):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for fn in filenames:
            if fn.endswith(".md"):
                yield os.path.join(dirpath, fn)


def _read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError as exc:
        return "[REPOAUDIT READ ERROR: %s]" % exc


def inventory(root):
    """File count, total size, per-directory counts, largest files."""
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for fn in filenames:
            p = os.path.join(dirpath, fn)
            try:
                files.append((os.path.getsize(p), os.path.relpath(p, root)))
            except OSError:
                pass
    by_dir = {}
    for size, rel in files:
        top = rel.split(os.sep)[0]
        by_dir[top] = by_dir.get(top, 0) + 1
    files.sort(reverse=True)
    return {
        "file_count": len(files),
        "total_mb": round(sum(s for s, _ in files) / 1e6, 1),
        "files_by_top_dir": dict(sorted(by_dir.items())),
        "largest_10": [(rel, size) for size, rel in files[:10]],
    }


def git_state(root):
    """Sync and cleanliness. The Sep 23 audit's first catch lived here:
    a remediation edit sitting uncommitted in the working tree."""
    out = {}
    try:
        out["status_porcelain"] = subprocess.run(
            ["git", "status", "--porcelain"], cwd=root, capture_output=True,
            text=True, check=True).stdout.strip()
        out["head"] = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=root, capture_output=True,
            text=True, check=True).stdout.strip()[:12]
        out["origin"] = subprocess.run(
            ["git", "rev-parse", "origin/main"], cwd=root, capture_output=True,
            text=True, check=True).stdout.strip()[:12]
        out["in_sync"] = out["head"] == out["origin"]
        out["clean"] = out["status_porcelain"] == ""
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        out["error"] = "git unavailable or not a repo: %s" % exc
    return out


def emdash_scan(root, exempt_globs=()):
    """Em-dash lines in markdown, minus exempted path globs.

    The house rule is grep-0 for composed documents, but verbatim quotes
    and machine-generated session files legitimately carry them. This
    check flags; the human ledger applies the exemption ruling.
    """
    hits = []
    for path in _iter_md(root):
        rel = os.path.relpath(path, root)
        if any(fnmatch.fnmatch(rel, g) for g in exempt_globs):
            continue
        for i, line in enumerate(_read(path).splitlines(), 1):
            if "\u2014" in line:
                hits.append({"file": rel, "line": i, "text": line.strip()[:120]})
    return hits


def marker_scan(root, include_tbd=False):
    """TODO/FIXME/XXX (optionally TBD) in live markdown."""
    markers = _MARKERS + (("TBD",) if include_tbd else ())
    hits = []
    for path in _iter_md(root):
        rel = os.path.relpath(path, root)
        for i, line in enumerate(_read(path).splitlines(), 1):
            for m in markers:
                if m in line:
                    hits.append({"file": rel, "line": i, "marker": m,
                                 "text": line.strip()[:120]})
                    break
    return hits


def name_scan(root, terms):
    """Scan for caller-supplied terms. Terms come from --terms-file at
    run time and are NEVER shipped in this repo (the tool is public;
    the term list is sensitive). Empty terms -> SKIPPED, not silent."""
    if not terms:
        return {"skipped": "no terms file supplied; name scan not run"}
    hits = []
    lowered = [t.lower() for t in terms]
    for path in _iter_md(root):
        rel = os.path.relpath(path, root)
        for i, line in enumerate(_read(path).splitlines(), 1):
            low = line.lower()
            for t in lowered:
                if t in low:
                    hits.append({"file": rel, "line": i, "term": t,
                                 "text": line.strip()[:120]})
                    break
    return hits


def link_check(root):
    """Relative markdown links that do not resolve on disk."""
    bad = []
    for path in _iter_md(root):
        rel_dir = os.path.dirname(path)
        for m in _LINK_RE.finditer(_read(path)):
            target = m.group(1).strip()
            if not target:
                continue
            resolved = os.path.normpath(os.path.join(rel_dir, target))
            if not os.path.exists(resolved):
                bad.append({"file": os.path.relpath(path, root),
                            "target": target})
    return bad


def tracked_artifacts(root):
    """Committed files that should never have been committed."""
    try:
        tracked = subprocess.run(
            ["git", "ls-files"], cwd=root, capture_output=True, text=True,
            check=True).stdout.splitlines()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {"skipped": "git unavailable; tracked-artifact check not run"}
    import fnmatch as _fm
    patterns = ["*.pyc", "*__pycache__*", "*.DS_Store", "*.tmp"]
    return [f for f in tracked
            if any(_fm.fnmatch(f, p) or p.rstrip("*").rstrip(".") in f
                   for p in patterns)]


def status_sweep(root, subdirs=("briefs",)):
    """Status line + last-commit date per brief. Staleness is a human
    call; this check just puts the two facts side by side."""
    rows = []
    for sub in subdirs:
        d = os.path.join(root, sub)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not (fn.endswith(".md") and fn[0].isdigit()):
                continue
            path = os.path.join(d, fn)
            status = ""
            for line in _read(path).splitlines()[:12]:
                if "status" in line.lower():
                    status = line.strip()[:160]
                    break
            try:
                date = subprocess.run(
                    ["git", "log", "-1", "--format=%cs", "--", path],
                    cwd=root, capture_output=True, text=True,
                    check=True).stdout.strip()
            except (subprocess.CalledProcessError, FileNotFoundError):
                date = "unknown"
            rows.append({"file": "%s/%s" % (sub, fn), "last_commit": date,
                         "status_line": status})
    return rows


def run_tests(root, suites):
    """Run-the-artifact step: execute each suite's file directly.

    The Sep 23 audit found unittest discover returns 0 tests (tests/
    lack __init__.py) while direct execution passes; the direct
    invocation is the documented one here.
    """
    results = []
    for suite in suites:
        path = os.path.join(root, suite)
        if not os.path.exists(path):
            results.append({"suite": suite, "result": "SKIPPED",
                            "detail": "file not found"})
            continue
        try:
            proc = subprocess.run(
                ["python3", path], cwd=os.path.dirname(path),
                capture_output=True, text=True, timeout=120)
            tail = (proc.stdout + proc.stderr).strip().splitlines()
            results.append({
                "suite": suite,
                "result": "PASS" if proc.returncode == 0 else "FAIL",
                "detail": tail[-1] if tail else "(no output)"})
        except subprocess.TimeoutExpired:
            results.append({"suite": suite, "result": "FAIL",
                            "detail": "timed out"})
    return results
