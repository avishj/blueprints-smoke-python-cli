# SPDX-FileCopyrightText: 2026 Avish J <avish.j@pm.me>
#
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for application configuration."""

import pytest

from blueprints_smoke_python_cli.config import Settings

pytestmark = pytest.mark.unit


def test_defaults(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("BLUEPRINTS_SMOKE_PYTHON_CLI_VERBOSE", raising=False)
    s = Settings()
    assert s.verbose is False


def test_env_prefix(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("BLUEPRINTS_SMOKE_PYTHON_CLI_VERBOSE", "1")
    s = Settings()
    assert s.verbose is True


def test_env_without_prefix_ignored(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("BLUEPRINTS_SMOKE_PYTHON_CLI_VERBOSE", raising=False)
    monkeypatch.setenv("VERBOSE", "true")
    s = Settings()
    assert s.verbose is False
