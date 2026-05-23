# SPDX-FileCopyrightText: 2026 Avish J <avish.j@pm.me>
#
# SPDX-License-Identifier: AGPL-3.0-or-later

set dotenv-load

default:
    @just --list

install:
    uv sync --frozen
    uvx --with pre-commit-uv==4.2.1 pre-commit@4.6.0 install --install-hooks

lint:
    uvx --with pre-commit-uv==4.2.1 pre-commit@4.6.0 run --all-files


test *args:
    uv run pytest --cov --cov-report=term -n auto {{ args }}

build:
    uv build
    uvx twine@6.2.0 check dist/*
    uv run --with dist/*.whl --no-project -- blueprints-smoke-python-cli --help

docs:
    uv run zensical build
    uv run zensical serve

ci:
    uvx --with pre-commit-uv==4.2.1 pre-commit@4.6.0 run --all-files
    uv run pytest --cov --cov-report=term --cov-report=html --cov-fail-under=70 -n auto
    just build
    uv run zensical build

clean:
    rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .ruff_cache/ .coverage htmlcov/ coverage.xml results.xml site/ .ty/ .complexipy_cache/
