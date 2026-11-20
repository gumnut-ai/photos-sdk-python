## Setting up the environment

We use [uv](https://docs.astral.sh/uv/) 0.13.6 or newer to manage dependencies because it will automatically provision a Python environment with the expected Python version. To set it up, run:

```sh
$ ./scripts/bootstrap
```

Bootstrap creates `uv.lock` only for a fresh SDK. Commit that lockfile; subsequent installs enforce it with `--locked`. Dependencies must satisfy the project's 14-day release cutoff.

With a committed lockfile, [install uv manually](https://docs.astral.sh/uv/getting-started/installation/) and run:

```sh
$ uv sync --locked --all-extras
```

You can then run scripts using `uv run --locked python script.py` or by manually activating the virtual environment:

```sh
# manually activate - https://docs.python.org/3/library/venv.html#how-venvs-work
$ source .venv/bin/activate

# now you can omit the `uv run` prefix
$ python script.py
```

## Modifying/Adding code

Most of the SDK is generated code. Modifications to code will be persisted between generations, but may
result in merge conflicts between manual patches and changes from the generator.

## Using the repository from source

If you’d like to use the repository from source, you can either install from git or link to a cloned repository:

To install via git:

```sh
$ pip install git+ssh://git@github.com/gumnut-ai/photos-sdk-python.git
```

Alternatively, you can build from source and install the wheel file:

Building this package will create two files in the `dist/` directory, a `.tar.gz` containing the source files and a `.whl` that can be used to install the package efficiently.

To create a distributable version of the library, all you have to do is run this command:

```sh
$ uv build
$ ./scripts/check-package
```

The package check installs the wheel and source archive separately into clean temporary
environments outside the checkout, using only base runtime dependencies. It checks installed
imports, version metadata, `py.typed`, and synchronous/asynchronous client lifecycle without
API requests. It requires exactly one of each artifact in `dist/`; use
`uv build --out-dir <empty-directory>` and `./scripts/check-package <directory>` if older
builds are present. Dependency resolution retains the 14-day release cutoff.

Then to install:

```sh
$ pip install ./path-to-wheel-file.whl
```

## Running tests

Tests require Node.js 24 and npm for [Steady](https://github.com/dgellow/steady),
the pinned local mock server. `scripts/test` starts an isolated server using the
embedded OpenAPI specification, runs the Python/Pydantic matrix, and stops the
server when testing finishes. It overrides `TEST_API_BASE_URL` and
`STAINLESS_OPENAPI_SPEC_URL` so the suite uses only its owned loopback server.
The first run downloads the pinned mock CLI; Python dependencies remain managed by uv.

```sh
$ ./scripts/test
```

## Linting and formatting

This repository uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting.
The lint script checks source, tests, and examples with [ty](https://docs.astral.sh/ty/),
targeting Python 3.11. ty errors fail the gate, while migration warnings remain visible.
The ty development dependency is pinned to a release at least 14 days old.
uv also excludes releases newer than 14 days when resolving dependencies.

To lint:

```sh
$ ./scripts/lint
```

To format and fix all ruff issues automatically:

```sh
$ ./scripts/format
```

## Publishing and releases

Merging the automated release PR creates a GitHub release, which runs [the `Publish PyPI` workflow](https://www.github.com/gumnut-ai/photos-sdk-python/actions/workflows/publish-pypi.yml) to publish to PyPI.
It publishes with trusted publishing (OIDC), so no registry token is stored.
The publish job runs in the protected `release` environment and waits until a maintainer approves the deployment.

If publishing fails, fix the cause and re-run the failed workflow run, which waits for approval again. There is no manual publish script.
