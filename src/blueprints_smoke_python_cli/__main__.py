# SPDX-FileCopyrightText: 2026 Avish J <avish.j@pm.me>
#
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Allow running as `python -m blueprints_smoke_python_cli`."""

from blueprints_smoke_python_cli.cli import app

app.meta()
