#!/usr/bin/env bash
export PYTEST_DISABLE_PLUGIN_AUTOLOAD="${PYTEST_DISABLE_PLUGIN_AUTOLOAD:-1}"
cd "$(dirname "$0")/.."
exec python3 -m pytest "$@"
