<!--
SPDX-FileCopyrightText: 2026 Avish J <avish.j@pm.me>

SPDX-License-Identifier: AGPL-3.0-or-later
-->

# blueprints-smoke-python-cli

[![CI](https://github.com/avishj/blueprints-smoke-python-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/avishj/blueprints-smoke-python-cli/actions/workflows/ci.yml)
[![CodeQL](https://github.com/avishj/blueprints-smoke-python-cli/actions/workflows/_codeql.yml/badge.svg)](https://github.com/avishj/blueprints-smoke-python-cli/actions/workflows/_codeql.yml)
[![codecov](https://codecov.io/gh/avishj/blueprints-smoke-python-cli/branch/main/graph/badge.svg)](https://codecov.io/gh/avishj/blueprints-smoke-python-cli)
[![PyPI](https://img.shields.io/pypi/v/blueprints-smoke-python-cli)](https://pypi.org/project/blueprints-smoke-python-cli/)
[![Downloads](https://img.shields.io/pypi/dm/blueprints-smoke-python-cli)](https://pypi.org/project/blueprints-smoke-python-cli/)
[![Python](https://img.shields.io/pypi/pyversions/blueprints-smoke-python-cli)](https://pypi.org/project/blueprints-smoke-python-cli/)
[![License](https://img.shields.io/github/license/avishj/blueprints-smoke-python-cli)](LICENSE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/avishj/blueprints-smoke-python-cli/badge)](https://scorecard.dev/viewer/?uri=github.com/avishj/blueprints-smoke-python-cli)
[![Docker Hub](https://img.shields.io/docker/v/avishj/blueprints-smoke-python-cli?label=docker%20hub)](https://hub.docker.com/r/avishj/blueprints-smoke-python-cli)
[![GHCR](https://ghcr-badge.egpl.dev/avishj/blueprints-smoke-python-cli/latest_tag?label=ghcr)](https://github.com/avishj/blueprints-smoke-python-cli/pkgs/container/blueprints-smoke-python-cli)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=avishj_blueprints-smoke-python-cli&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=avishj_blueprints-smoke-python-cli)

A CLI application.

## Features

- Subcommand-based CLI built with [Cyclopts](https://cyclopts.readthedocs.io/)
- Rich terminal output via [Rich](https://rich.readthedocs.io/)
- Typed configuration from environment variables and `.env` files via [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- Fully typed with [PEP 561](https://peps.python.org/pep-0561/) `py.typed` marker
- Python 3.13+ support

## Installation

```bash
uv tool install blueprints-smoke-python-cli
```

Or with pip:

```bash
pip install blueprints-smoke-python-cli
```

Or with Docker:

```bash
docker run --rm ghcr.io/avishj/blueprints-smoke-python-cli --help
# or
docker run --rm docker.io/avishj/blueprints-smoke-python-cli --help
```

## Usage

```bash
blueprints-smoke-python-cli --help
blueprints-smoke-python-cli hello World
```

## Development

### Prerequisites

- [uv](https://docs.astral.sh/uv/)
- [just](https://github.com/casey/just)

### Setup

```bash
git clone https://github.com/avishj/blueprints-smoke-python-cli.git
cd blueprints-smoke-python-cli
just install
```

### Common tasks

```bash
just install # sync dependencies and install git hooks
just lint    # run all pre-commit hooks (ruff, ty, complexipy, reuse, etc.)
just test    # run all tests with coverage
just build   # build sdist + wheel, twine check, entry point smoke test
just docs    # build and serve docs locally
just ci      # full composite gate (lint + test + build + docs)
just clean   # remove build artifacts
```

## Configuration

blueprints-smoke-python-cli reads configuration from environment variables prefixed with `BLUEPRINTS_SMOKE_PYTHON_CLI_` and from `.env` files.

| Variable | Default | Description |
| --- | --- | --- |
| `BLUEPRINTS_SMOKE_PYTHON_CLI_VERBOSE` | `false` | Enable verbose output |

## Documentation

[https://avishj.github.io/blueprints-smoke-python-cli](https://avishj.github.io/blueprints-smoke-python-cli)

## Contributing

Contributions are welcome. Please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/my-feature`)
3. Run `just install`, make your changes, and run `just ci` to verify
4. Commit using [conventional commits](https://www.conventionalcommits.org/)
5. Open a pull request

## License

[AGPL-3.0-or-later](LICENSE)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=avishj/blueprints-smoke-python-cli&type=Date)](https://star-history.com/#avishj/blueprints-smoke-python-cli&Date)

<!-- verify 2026-05-23T07:15:47.332230+00:00 -->
