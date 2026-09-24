# pushgate (pre-push discipline gate) · module pushgate

Part of the ThreadCat lab tooling. Free, local, stdlib-only Python. No cat name:
pushgate joined the family after the nine were named, and the naming convention
belongs to the nine-cat set.

## Status: EXPERIMENTAL (self-tested Sep 24, not yet field-run). Canonical standing: see TOOL-STATUS.md.

A git pre-push gate born from a day with three fails of one class: an em-dash
check that printed findings while the push ran anyway (twice), and an unscoped
`git add` that swept another lane's working files into a push (error 16). The
design fix is structural: the check runs as the hook, so its exit code STOPS
the push instead of narrating it.

What it does: lists the staged files, sweeps exactly those (never the whole
tree, so other lanes' uncommitted work stays invisible), blocks on em-dash
findings, and prints the staged diff --stat for the review-before-push rule.

Install from the repo root:

    echo 'python3 tools/pushgate/pushgate.py --staged' > .git/hooks/pre-push
    chmod +x .git/hooks/pre-push

Bypass with `git push --no-verify`, which is what the bypass is for: a
recorded exception with an error-log line, not a habit.

Tested: 4 controls (dirty file blocked, clean file passes, missing staged
file flagged without crashing, exit codes correct) plus live smoke on the
real index in both modes.
