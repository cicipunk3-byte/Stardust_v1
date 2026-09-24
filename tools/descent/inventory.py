#!/usr/bin/env python3
"""Descent inventory — ATC Local Descent Plan v0.1, step 1.

Read-only machine inventory: hardware, OS, storage, memory, network,
runtimes, services, ports, and known world substrates (Stardew/SMAPI).
No installs, no writes outside the chosen output directory, no network.
Run it on the downstairs machine; it reports what IS, not what to install.

Usage:
    python3 inventory.py --out ./descent-inventory
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

READ_ONLY = True  # this script must never gain a write outside --out


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def run(cmd: list[str]) -> str | None:
    """Best-effort read-only command probe. Returns None on any failure."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            return result.stdout.strip()
        return None
    except (OSError, subprocess.TimeoutExpired):
        return None


def probe_system() -> dict[str, Any]:
    info: dict[str, Any] = {
        "platform": platform.platform(),
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "hostname": platform.node(),
        "python_version": platform.python_version(),
    }
    if platform.system() == "Darwin":
        info["macos_version"] = run(["sw_vers", "-productVersion"])
        info["macos_build"] = run(["sw_vers", "-buildVersion"])
        info["hardware_overview"] = run(
            ["system_profiler", "SPHardwareDataType", "-json"]
        )
        if info["hardware_overview"]:
            try:
                info["hardware_overview"] = json.loads(info["hardware_overview"])
            except json.JSONDecodeError:
                pass
        info["storage"] = run(["df", "-h", "/"])
        info["memory_pressure"] = run(["memory_pressure", "-Q"])
        info["listening_ports"] = run(["netstat", "-an", "-p", "tcp"])
    else:
        info["os_release"] = run(["cat", "/etc/os-release"])
        info["cpu_info"] = run(["cat", "/proc/cpuinfo"])
        info["storage"] = run(["df", "-h", "/"])
        info["memory"] = run(["free", "-h"])
        info["listening_ports"] = run(["ss", "-tuln"])
    return info


def probe_runtimes() -> dict[str, Any]:
    runtimes: dict[str, Any] = {}
    candidates = {
        "python3": ["python3", "--version"],
        "pip3": ["pip3", "--version"],
        "node": ["node", "--version"],
        "npm": ["npm", "--version"],
        "git": ["git", "--version"],
        "brew": ["brew", "--version"],
        "docker": ["docker", "--version"],
        "colima": ["colima", "version"],
        "ollama": ["ollama", "--version"],
        "smacli": ["smapi-cli", "--version"],
    }
    for name, cmd in candidates.items():
        found = shutil.which(cmd[0])
        runtimes[name] = {"installed": bool(found), "path": found, "version": run(cmd) if found else None}

    # ollama local model list (read-only query of local service)
    if runtimes["ollama"]["installed"]:
        runtimes["ollama_models"] = run(["ollama", "list"])
    return runtimes


def probe_processes() -> dict[str, Any]:
    """Do not assume an empty machine. What is already running?"""
    return {
        "top_processes": run(
            ["ps", "-Ao", "pid,pcpu,pmem,comm", "-r"]
        ),
        "homebrew_services": run(["brew", "services", "list"]),
        "launchctl_user": run(["launchctl", "list"]),
    }


def probe_world_substrate(home: Path) -> dict[str, Any]:
    """Look for Stardew / SMAPI without assuming install location."""
    hits: dict[str, Any] = {"stardew": None, "smapi": None}
    search_roots = [home / "Library" / "Application Support" / "Steam",
                    home / ".steam", home / ".config" / "StardewValley",
                    Path("/Applications")]
    for root in search_roots:
        if root.exists():
            hits[f"exists:{root}"] = True
    app = Path("/Applications/Stardew Valley.app")
    hits["stardew"] = str(app) if app.exists() else None
    smapi_mods = home / "Library" / "Application Support" / "StardewValley" / "Mods"
    hits["smapi_mods_dir"] = str(smapi_mods) if smapi_mods.exists() else None
    if hits["smapi_mods_dir"]:
        try:
            hits["smapi_mods"] = sorted(p.name for p in smapi_mods.iterdir())
        except OSError:
            hits["smapi_mods"] = "unreadable"
    return hits


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Descent Inventory",
        "",
        f"- **Date:** {report['timestamp']}",
        f"- **Machine:** {report['system'].get('hostname', 'unknown')}",
        f"- **Platform:** {report['system'].get('platform', 'unknown')}",
        f"- **Read-only run:** yes (no installs, no writes outside output dir)",
        "",
        "## Storage",
        "```",
        report["system"].get("storage") or "unavailable",
        "```",
        "",
        "## Runtimes",
        "",
        "| tool | installed | version |",
        "|------|-----------|---------|",
    ]
    for name, data in report["runtimes"].items():
        if isinstance(data, dict):
            lines.append(f"| {name} | {'yes' if data['installed'] else 'no'} | {data.get('version') or '-'} |")
    lines += [
        "",
        "## Existing world substrate",
        "",
    ]
    substrate = report.get("world_substrate", {})
    for key, value in substrate.items():
        lines.append(f"- **{key}:** {value}")
    lines += [
        "",
        "## Already running (do not assume an empty machine)",
        "",
        "```",
        (report["processes"].get("top_processes") or "unavailable")[:2000],
        "```",
        "",
        "---",
        "",
        "_Full raw report: `inventory-report.json` alongside this file._",
        "",
        "_Descent plan rule: no installs, no architecture improvisation. We look first._",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only descent inventory (no installs)")
    parser.add_argument("--out", type=Path, default=Path("./descent-inventory"),
                        help="output directory (the only path written)")
    args = parser.parse_args()

    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    home = Path.home()

    report: dict[str, Any] = {
        "schema_version": "0.1",
        "timestamp": now(),
        "system": probe_system(),
        "runtimes": probe_runtimes(),
        "processes": probe_processes(),
        "world_substrate": probe_world_substrate(home),
        "network_interfaces": run(["ifconfig"]) or run(["ip", "addr"]),
    }

    json_path = out / "inventory-report.json"
    json_path.write_text(json.dumps(report, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")
    md_path = out / "INVENTORY.md"
    md_path.write_text(render_markdown(report), encoding="utf-8")

    print(f"inventory written: {json_path}\n                    {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
