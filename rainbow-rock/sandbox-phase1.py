#!/usr/bin/env python3
"""Phase-1 Rainbow Rock sandbox: a local, dependency-free lifecycle world.

This program deliberately has no network, model, shell, or game integration.
It owns only its selected data directory and provides the lifecycle operations
needed before any agent or mutating world action is introduced.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "0.1"
WORLD_ID = "rainbow-rock-empty-world"
WORLD_VERSION = "0.1-phase-1"


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex}"


class Sandbox:
    def __init__(self, data_dir: Path) -> None:
        self.root = data_dir.resolve()
        self.state_path = self.root / "world" / "state.json"
        self.events_path = self.root / "world" / "events.jsonl"
        self.audit_path = self.root / "audit" / "events.jsonl"
        self.snapshots_dir = self.root / "world" / "snapshots"
        self.exports_dir = self.root / "audit" / "exports"
        self.backups_dir = self.root / "backups"

    def setup(self) -> None:
        for directory in (
            self.state_path.parent,
            self.audit_path.parent,
            self.snapshots_dir,
            self.exports_dir,
            self.backups_dir,
        ):
            directory.mkdir(parents=True, exist_ok=True)

    def exists(self) -> bool:
        return self.state_path.exists()

    def baseline(self) -> dict[str, Any]:
        return {
            "schema_version": SCHEMA_VERSION,
            "world_id": WORLD_ID,
            "world_version": WORLD_VERSION,
            "session_id": new_id("session"),
            "status": "stopped",
            "created_at": now(),
            "updated_at": now(),
            "last_snapshot_id": None,
            "mutations_enabled": False,
            "declared_capabilities": [
                "system.start",
                "system.stop",
                "system.reset",
                "system.status",
                "system.snapshot",
                "system.export_audit",
            ],
        }

    def load_state(self) -> dict[str, Any]:
        if not self.exists():
            raise RuntimeError("sandbox is not initialized; run start first")
        try:
            return json.loads(self.state_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise RuntimeError(f"state is unreadable: {error}") from error

    def save_state(self, state: dict[str, Any]) -> None:
        state["updated_at"] = now()
        temporary = self.state_path.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        temporary.replace(self.state_path)

    def append(self, destination: Path, record: dict[str, Any]) -> None:
        with destination.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(record, sort_keys=True) + "\n")

    def record(self, event_type: str, detail: dict[str, Any]) -> dict[str, Any]:
        record = {
            "schema_version": SCHEMA_VERSION,
            "audit_id": new_id("audit"),
            "timestamp": now(),
            "world_id": WORLD_ID,
            "world_version": WORLD_VERSION,
            "event_type": event_type,
            "detail": detail,
        }
        self.append(self.events_path, {"world_event_id": new_id("world"), **record})
        self.append(self.audit_path, record)
        return record

    def snapshot(self, reason: str) -> dict[str, Any]:
        state = self.load_state()
        snapshot_id = new_id("snapshot")
        snapshot = {
            "schema_version": SCHEMA_VERSION,
            "snapshot_id": snapshot_id,
            "timestamp": now(),
            "reason": reason,
            "world_id": WORLD_ID,
            "world_version": WORLD_VERSION,
            "state": state,
        }
        target = self.snapshots_dir / f"{snapshot_id}.json"
        target.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        state["last_snapshot_id"] = snapshot_id
        self.save_state(state)
        self.record("snapshot.created", {"snapshot_id": snapshot_id, "reason": reason, "path": str(target)})
        return snapshot

    def start(self) -> dict[str, Any]:
        self.setup()
        state = self.baseline() if not self.exists() else self.load_state()
        if state["status"] == "running":
            return {"result": "already_running", "state": state}
        state["status"] = "running"
        self.save_state(state)
        self.record("system.started", {"session_id": state["session_id"]})
        snapshot = self.snapshot("start")
        return {"result": "started", "state": self.load_state(), "snapshot_id": snapshot["snapshot_id"]}

    def stop(self) -> dict[str, Any]:
        state = self.load_state()
        if state["status"] == "stopped":
            return {"result": "already_stopped", "state": state}
        state["status"] = "stopped"
        self.save_state(state)
        snapshot = self.snapshot("stop")
        self.record("system.stopped", {"session_id": state["session_id"], "snapshot_id": snapshot["snapshot_id"]})
        return {"result": "stopped", "state": self.load_state(), "snapshot_id": snapshot["snapshot_id"]}

    def export_audit(self, reason: str) -> Path:
        self.setup()
        target = self.exports_dir / f"audit_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}_{uuid.uuid4().hex[:8]}.jsonl"
        if self.audit_path.exists():
            shutil.copy2(self.audit_path, target)
        else:
            target.touch()
        self.record("audit.exported", {"reason": reason, "path": str(target)})
        return target

    def reset(self, confirmed: bool) -> dict[str, Any]:
        if not confirmed:
            raise RuntimeError("reset requires --confirm-reset; no change was made")
        self.load_state()
        backup = self.export_audit("pre-reset")
        old_session = self.load_state()["session_id"]
        state = self.baseline()
        self.save_state(state)
        self.record("system.reset", {"previous_session_id": old_session, "backup": str(backup)})
        snapshot = self.snapshot("reset")
        return {"result": "reset", "state": self.load_state(), "backup": str(backup), "snapshot_id": snapshot["snapshot_id"]}

    def status(self) -> dict[str, Any]:
        state = self.load_state()
        return {
            "state": state,
            "paths": {
                "root": str(self.root),
                "events": str(self.events_path),
                "audit": str(self.audit_path),
                "snapshots": str(self.snapshots_dir),
            },
            "network_access": "not implemented",
            "mutating_world_actions": "not implemented",
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Rainbow Rock Phase-1 empty sandbox")
    parser.add_argument("--data-dir", type=Path, default=Path(".rainbow-rock-sandbox"), help="only directory this sandbox manages")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("start")
    commands.add_parser("stop")
    commands.add_parser("status")
    commands.add_parser("snapshot")
    commands.add_parser("export-audit")
    reset = commands.add_parser("reset")
    reset.add_argument("--confirm-reset", action="store_true")
    args = parser.parse_args()
    sandbox = Sandbox(args.data_dir)
    try:
        if args.command == "start":
            result: Any = sandbox.start()
        elif args.command == "stop":
            result = sandbox.stop()
        elif args.command == "status":
            result = sandbox.status()
        elif args.command == "snapshot":
            result = sandbox.snapshot("manual")
        elif args.command == "export-audit":
            result = {"audit_export": str(sandbox.export_audit("manual"))}
        else:
            result = sandbox.reset(args.confirm_reset)
    except RuntimeError as error:
        print(json.dumps({"result": "error", "message": str(error)}), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
