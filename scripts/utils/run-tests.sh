#!/usr/bin/env bash

set -e

cd "$(dirname "$0")/../.."



export DEFER_PYDANTIC_BUILD=false

# Note that we need to specify the patch version here so that uv
# won't use unstable (alpha, beta, rc) releases for the tests
# (one pinned release per supported minor version, lowest first)
PY_VERSIONS=(3.11.18 3.12.16 3.13.18 3.14.10 3.15.2)

function run_tests() {
    echo "==> Running tests with Pydantic v2"
    uv run --locked --isolated --all-extras pytest "$@"

    echo "==> Running tests with Pydantic v1"
    uv run --locked --isolated --all-extras --group=pydantic-v1 pytest "$@"
}

# If UV_PYTHON is already set in the environment, just run the command once
if [[ -n "$UV_PYTHON" ]]; then
  run_tests "$@"
else
  # If UV_PYTHON is not set, run the command for every supported version
  for version in "${PY_VERSIONS[@]}"; do
    echo "==> Running tests for Python $version"
    UV_PYTHON="$version" run_tests "$@"
  done
fi
