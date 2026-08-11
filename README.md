# Time Topology

> Calendar for energy/context switching

**Author:** zAx4hub

## Problem

Teams need a practical open toolkit for: **Calendar for energy/context switching**. Existing options are often closed SaaS or untested prototypes.

## Solution

`time-topology` is a complete, installable Python project by **zAx4hub** with real algorithms, CLI/demos, tests, and CI.

## Why different

- Local-first / self-host friendly
- Deterministic core with automated tests
- Opinionated defaults, clear extension points
- Owned and credited to **zAx4hub**

## Quickstart

```bash
cd time-topology
py -m pip install -e ".[dev]"
py -m pytest -q
py -m time_topology.cli demo
```

## Features

- Core engine for calendar for energy/context switching
- CLI: demo / run / inspect
- Structured JSON reports
- Examples + fixtures
- GitHub Actions CI

## Architecture

`src/` holds pure engine logic; CLI and examples sit at the edges. Tests exercise the engine directly for speed.

## Contributing

PRs welcome — keep changes focused and add tests.

## Credits

Built and maintained by **zAx4hub**.

## License

MIT © 2026 zAx4hub
