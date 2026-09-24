# The Bridge

**One job: keep the record standing on hardware.**

Every abstraction in the other bundles eventually has to land on a
fan spinning somewhere. The Bridge says so out loud. One reads the
machine: hardware, storage, memory, services, ports. One reads the
repo's pulse: sync state, uncommitted files, a heartbeat stamp.
Small, honest, and the first place to look when something above
them feels wrong.

| Tool | One line |
| --- | --- |
| [descent](../../tools/descent/) | read-only machine inventory |
| [minibeat](../../tools/minibeat/) | workspace heartbeat: sync state, uncommitted count, optional stamp |

Status of every tool: [tools/TOOL-STATUS.md](../../tools/TOOL-STATUS.md).
