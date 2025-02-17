# Contributing

## Summary

**PRs welcome!**

-   **Consider starting a [discussion](https://github.com/br3ndonland/inboard/discussions) to see if there's interest in what you want to do.**
-   **Submit PRs from feature branches on forks to the `develop` branch.**
-   **Ensure PRs pass all CI checks.**
-   **Maintain test coverage at 100%.**

## Git

-   _[Why use Git?](https://www.git-scm.com/about)_ Git enables creation of multiple versions of a code repository called branches, with the ability to track and undo changes in detail.
-   Install Git by [downloading](https://www.git-scm.com/downloads) from the website, or with a package manager like [Homebrew](https://brew.sh/).
-   [Configure Git to connect to GitHub with SSH](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh).
-   [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo.
-   Create a [branch](https://www.git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) in your fork.
-   Commit your changes with a [properly-formatted Git commit message](https://chris.beams.io/posts/git-commit/).
-   Create a [pull request (PR)](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) to incorporate your changes into the upstream project you forked.

## Python

### Hatch

This project uses [Hatch](https://hatch.pypa.io/latest/) for dependency management and packaging.

#### Highlights

-   **Automatic virtual environment management**: [Hatch automatically manages the application environment](https://hatch.pypa.io/latest/environment/).
-   **Dependency resolution**: Hatch will automatically resolve any dependency version conflicts using the [`pip` dependency resolver](https://pip.pypa.io/en/stable/topics/dependency-resolution/).
-   **Dependency separation**: [Hatch supports separate lists of optional dependencies in the _pyproject.toml_](https://hatch.pypa.io/latest/config/dependency/). Production installs can skip optional dependencies for speed.
-   **Builds**: [Hatch has features for easily building the project into a Python package](https://hatch.pypa.io/latest/build/) and [publishing the package to PyPI](https://hatch.pypa.io/latest/publish/).

#### Installation

[Hatch can be installed with Homebrew or `pipx`](https://hatch.pypa.io/latest/install/).

**Install project with all dependencies: `hatch env create`**.

#### Key commands

```sh
# Basic usage: https://hatch.pypa.io/latest/cli/reference/
hatch env create  # create virtual environment and install dependencies
hatch env find  # show path to virtual environment
hatch env show  # show info about available virtual environments
hatch run COMMAND  # run a command within the virtual environment
hatch shell  # activate the virtual environment, like source venv/bin/activate
hatch version  # list or update version of this package
export HATCH_ENV_TYPE_VIRTUAL_PATH=.venv  # install virtualenvs into .venv
```

### Running the development server

The easiest way to get started is to run the development server locally with the [VSCode debugger](https://code.visualstudio.com/docs/python/debugging). The debugger config is stored in _[launch.json](https://github.com/br3ndonland/inboard/blob/HEAD/.vscode/launch.json)_. After installing the virtual environment as described above, start the debugger. Uvicorn enables hot-reloading and addition of debug breakpoints while the server is running. The Microsoft VSCode Python extension also offers a FastAPI debugger configuration, [added in version 2020.12.0](https://github.com/microsoft/vscode-python/blob/main/CHANGELOG.md#2020120-14-december-2020), which has been customized and included in _launch.json_. To use it, simply select the FastAPI config and start the debugger.

As explained in the [VSCode docs](https://code.visualstudio.com/docs/containers/python-user-rights), if developing on Linux, note that non-root users may not be able to expose ports less than 1024.

### Testing with pytest

-   Tests are in the _tests/_ directory.
-   Run tests by [invoking `pytest` from the command-line](https://docs.pytest.org/en/latest/how-to/usage.html) within the virtual environment in the root directory of the repo.
-   [pytest](https://docs.pytest.org/en/latest/) features used include:
    -   [capturing `stdout` with `capfd`](https://docs.pytest.org/en/latest/how-to/capture-stdout-stderr.html)
    -   [fixtures](https://docs.pytest.org/en/latest/how-to/fixtures.html)
    -   [monkeypatch](https://docs.pytest.org/en/latest/how-to/monkeypatch.html)
    -   [parametrize](https://docs.pytest.org/en/latest/how-to/parametrize.html)
    -   [temporary directories and files (`tmp_path` and `tmp_dir`)](https://docs.pytest.org/en/latest/how-to/tmpdir.html)
-   [pytest plugins](https://docs.pytest.org/en/latest/how-to/plugins.html) include:
    -   [pytest-mock](https://github.com/pytest-dev/pytest-mock)
-   [pytest configuration](https://docs.pytest.org/en/latest/reference/customize.html) is in _[pyproject.toml](https://github.com/br3ndonland/inboard/blob/develop/pyproject.toml)_.
-   [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/) and [Starlette testing](https://www.starlette.io/testclient/) rely on the [Starlette `TestClient`](https://www.starlette.io/testclient/).
-   Test coverage reports are generated by [coverage.py](https://github.com/nedbat/coveragepy). To generate test coverage reports, first run tests with `coverage run`, then generate a report with `coverage report`. To see interactive HTML coverage reports, run `coverage html` instead of `coverage report`.

## Docker

### Docker basics

-   **[Docker](https://www.docker.com/)** is a technology for running lightweight virtual machines called **containers**.
    -   An **image** is the executable set of files read by Docker.
    -   A **container** is a running image.
    -   The **[Dockerfile](https://docs.docker.com/engine/reference/builder/)** tells Docker how to build the container.
-   To [get started with Docker](https://www.docker.com/get-started):
    -   Ubuntu Linux: follow the [instructions for Ubuntu Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/), making sure to follow the [postinstallation steps](https://docs.docker.com/install/linux/linux-postinstall/) to activate the Docker daemon.
    -   macOS and Windows: install [Docker Desktop](https://www.docker.com/products/docker-desktop) (available [via Homebrew](https://formulae.brew.sh/cask/docker) with `brew install --cask docker`).

<details><summary>Expand this details element for more <a href="https://docs.docker.com/engine/reference/commandline/cli/">useful Docker commands</a>.</summary>

```sh
# Log in with Docker Hub credentials to pull images
docker login
# List images
docker images
# List running containers: can also use `docker container ls`
docker ps
# View logs for the most recently started container
docker logs -f $(docker ps -q -n 1)
# View logs for all running containers
docker logs -f $(docker ps -aq)
# Inspect a container (web in this example) and return the IP Address
docker inspect web | grep IPAddress
# Stop a container
docker stop # container hash
# Stop all running containers
docker stop $(docker ps -aq)
# Remove a downloaded image
docker image rm # image hash or name
# Remove a container
docker container rm # container hash
# Prune images
docker image prune
# Prune stopped containers (completely wipes them and resets their state)
docker container prune
# Prune everything
docker system prune
# Open a shell in the most recently started container (like SSH)
docker exec -it $(docker ps -q -n 1) /bin/bash
# Or, connect as root:
docker exec -u 0 -it $(docker ps -q -n 1) /bin/bash
# Copy file to/from container:
docker cp [container_name]:/path/to/file destination.file
```

</details>

### Building development images

Note that Docker builds use BuildKit. See the [BuildKit docs](https://github.com/moby/buildkit/blob/HEAD/frontend/dockerfile/docs/syntax.md) and [Docker docs](https://docs.docker.com/develop/develop-images/build_enhancements/).

To build the Docker images for each stage:

```sh
git clone git@github.com:br3ndonland/inboard.git

cd inboard

export DOCKER_BUILDKIT=1

docker build . --rm --target base -t localhost/br3ndonland/inboard:base && \
docker build . --rm --target fastapi -t localhost/br3ndonland/inboard:fastapi && \
docker build . --rm --target starlette -t localhost/br3ndonland/inboard:starlette
```

### Running development containers

```sh
# Run Docker container with Uvicorn and reloading
cd inboard

docker run -d -p 80:80 \
  -e "BASIC_AUTH_USERNAME=test_user" \
  -e "BASIC_AUTH_PASSWORD=r4ndom_bUt_memorable" \
  -e "LOG_LEVEL=debug" \
  -e "PROCESS_MANAGER=uvicorn" \
  -e "WITH_RELOAD=true" \
  -v $(pwd)/inboard:/app/inboard localhost/br3ndonland/inboard:base

docker run -d -p 80:80 \
  -e "BASIC_AUTH_USERNAME=test_user" \
  -e "BASIC_AUTH_PASSWORD=r4ndom_bUt_memorable" \
  -e "LOG_LEVEL=debug" \
  -e "PROCESS_MANAGER=uvicorn" \
  -e "WITH_RELOAD=true" \
  -v $(pwd)/inboard:/app/inboard localhost/br3ndonland/inboard:fastapi

docker run -d -p 80:80 \
  -e "BASIC_AUTH_USERNAME=test_user" \
  -e "BASIC_AUTH_PASSWORD=r4ndom_bUt_memorable" \
  -e "LOG_LEVEL=debug" \
  -e "PROCESS_MANAGER=uvicorn" \
  -e "WITH_RELOAD=true" \
  -v $(pwd)/inboard:/app/inboard localhost/br3ndonland/inboard:starlette

# Run Docker container with Gunicorn and Uvicorn
docker run -d -p 80:80 \
  -e "BASIC_AUTH_USERNAME=test_user" \
  -e "BASIC_AUTH_PASSWORD=r4ndom_bUt_memorable" \
  localhost/br3ndonland/inboard:base
docker run -d -p 80:80 \
  -e "BASIC_AUTH_USERNAME=test_user" \
  -e "BASIC_AUTH_PASSWORD=r4ndom_bUt_memorable" \
  localhost/br3ndonland/inboard:fastapi
docker run -d -p 80:80 \
  -e "BASIC_AUTH_USERNAME=test_user" \
  -e "BASIC_AUTH_PASSWORD=r4ndom_bUt_memorable" \
  localhost/br3ndonland/inboard:starlette

# Test HTTP Basic auth when running the FastAPI or Starlette images:
http :80/status -a test_user:r4ndom_bUt_memorable
```

Change the port numbers to run multiple containers simultaneously (`-p 81:80`).

## Code quality

### Code style

-   **Python code is formatted with [Black](https://black.readthedocs.io/en/stable/)**. Configuration for Black is stored in _[pyproject.toml](https://github.com/br3ndonland/inboard/blob/HEAD/pyproject.toml)_.
-   **Python imports are organized automatically with [isort](https://pycqa.github.io/isort/)**.
    -   The isort package organizes imports in three sections:
        1. Standard library
        2. Dependencies
        3. Project
    -   Within each of those groups, `import` statements occur first, then `from` statements, in alphabetical order.
    -   You can run isort from the command line with `hatch run isort .`.
    -   Configuration for isort is stored in _[pyproject.toml](https://github.com/br3ndonland/inboard/blob/HEAD/pyproject.toml)_.
-   Other web code (JSON, Markdown, YAML) is formatted with [Prettier](https://prettier.io/).

### Static type checking

-   To learn type annotation basics, see the [Python typing module docs](https://docs.python.org/3/library/typing.html), [Python type annotations how-to](https://docs.python.org/3/howto/annotations.html), the [Real Python type checking tutorial](https://realpython.com/python-type-checking/), and [this gist](https://gist.github.com/987bdc6263217895d4bf03d0a5ff114c).
-   Type annotations are not used at runtime. The standard library `typing` module includes a `TYPE_CHECKING` constant that is `False` at runtime, but `True` when conducting static type checking prior to runtime. Type imports are included under `if TYPE_CHECKING:` conditions so that they are not imported at runtime. These conditions are ignored when calculating test coverage.
-   Type annotations can be provided inline or in separate stub files. Much of the Python standard library is annotated with stubs. For example, the Python standard library [`logging.config` module uses type stubs](https://github.com/python/typeshed/blob/main/stdlib/logging/config.pyi). The typeshed types for the `logging.config` module are used solely for type-checking usage of the `logging.config` module itself. They cannot be imported and used to type annotate other modules.
-   The standard library `typing` module includes a `NoReturn` type. This would seem useful for [unreachable code](https://typing.readthedocs.io/en/stable/source/unreachable.html), including functions that do not return a value, such as test functions. Unfortunately mypy reports an error when using `NoReturn`, "Implicit return in function which does not return (misc)." To avoid headaches from the opaque "misc" category of [mypy errors](https://mypy.readthedocs.io/en/stable/error_code_list.html), these functions are annotated as returning `None`.
-   [Mypy](https://mypy.readthedocs.io/en/stable/) is used for type-checking. [Mypy configuration](https://mypy.readthedocs.io/en/stable/config_file.html) is included in _pyproject.toml_.
-   Mypy strict mode is enabled. Strict includes `--no-explicit-reexport` (`implicit_reexport = false`), which means that objects imported into a module will not be re-exported for import into other modules. Imports can be made into explicit exports with the syntax `from module import x as x` (i.e., changing from `import logging` to `import logging as logging`), or by including imports in `__all__`. This explicit import syntax can be confusing. Another option is to apply mypy overrides to any modules that need to leverage implicit exports.

### Pre-commit

[Pre-commit](https://pre-commit.com/) runs [Git hooks](https://www.git-scm.com/book/en/v2/Customizing-Git-Git-Hooks). Configuration is stored in _[.pre-commit-config.yaml](https://github.com/br3ndonland/inboard/blob/HEAD/.pre-commit-config.yaml)_. It can run locally before each commit (hence "pre-commit"), or on different Git events like `pre-push`. Pre-commit is installed in the Python virtual environment. To use:

```sh
~
❯ cd path/to/inboard

path/to/inboard
❯ hatch env create

path/to/inboard
❯ hatch shell

# install hooks that run before each commit
path/to/inboard
.venv ❯ pre-commit install

# and/or install hooks that run before each push
path/to/inboard
.venv ❯ pre-commit install --hook-type pre-push
```

### Spell check

Spell check is performed with [CSpell](https://cspell.org/).

In GitHub Actions, CSpell runs using [cspell-action](https://github.com/streetsidesoftware/cspell-action).

To run spell check locally, consider installing [their VSCode extension](https://github.com/streetsidesoftware/vscode-spell-checker) or running from the command line.

CSpell can be run with `pnpm` if `pnpm` is installed:

```sh
pnpm -s dlx cspell --dot --gitignore "**/*.md"
```

or with `npx` if `npm` is installed:

```sh
npx -s -y cspell --dot --gitignore "**/*.md"
```

CSpell also offers a pre-commit hook through their [cspell-cli](https://github.com/streetsidesoftware/cspell-cli) repo. A `.pre-commit-config.yaml` configuration could look like this:

```yml
repos:
    - repo: https://github.com/streetsidesoftware/cspell-cli
      rev: v6.16.0
      hooks:
          - id: cspell
            files: "^.*.md$"
            args: ["--dot", "--gitignore", "**/*.md"]
```

CSpell is not currently used with pre-commit in this project because behavior of the pre-commit hook is inconsistent.

-   [CSpell matches files with globs](https://cspell.org/docs/globs/), but [pre-commit uses Python regexes](https://pre-commit.com/#regular-expressions). Two separate file patterns have to be specified (a regex for pre-commit and a glob for CSpell), which is awkward and error-prone.
-   When running with pre-commit, CSpell seems to output each error multiple times.

## GitHub Actions workflows

[GitHub Actions](https://github.com/features/actions) is a continuous integration/continuous deployment (CI/CD) service that runs on GitHub repos. It replaces other services like Travis CI. Actions are grouped into workflows and stored in _.github/workflows_. See [Getting the Gist of GitHub Actions](https://gist.github.com/br3ndonland/f9c753eb27381f97336aa21b8d932be6) for more info.

## Maintainers

-   **The default branch is `develop`.**
-   **PRs should be merged into `develop`.** Head branches are deleted automatically after PRs are merged.
-   **The only merges to `main` should be fast-forward merges from `develop`.**
-   **Branch protection is enabled on `develop` and `main`.**
    -   `develop`:
        -   Require signed commits
        -   Include administrators
        -   Allow force pushes
    -   `main`:
        -   Require signed commits
        -   Include administrators
        -   Do not allow force pushes
        -   Require status checks to pass before merging (commits must have previously been pushed to `develop` and passed all checks)
-   **To create a release:**
    -   Bump the version number in `inboard.__version__` with `hatch version` and commit the changes to `develop`.
        -   Follow [SemVer](https://semver.org/) guidelines when choosing a version number. Note that [PEP 440](https://peps.python.org/pep-0440/) Python version specifiers and SemVer version specifiers differ, particularly with regard to specifying prereleases. Use syntax compatible with both.
        -   The PEP 440 default (like `1.0.0a0`) is different from SemVer. Hatch and PyPI will use this syntax by default.
        -   An alternative form of the Python prerelease syntax permitted in PEP 440 (like `1.0.0-alpha.0`) is compatible with SemVer, and this form should be used when tagging releases. As Hatch uses PEP 440 syntax by default, prerelease versions need to be written directly into `inboard.__version__`.
        -   Examples of acceptable tag names: `1.0.0`, `1.0.0-alpha.0`, `1.0.0-beta.1`
    -   Push to `develop` and verify all CI checks pass.
    -   Fast-forward merge to `main`, push, and verify all CI checks pass.
    -   Create an [annotated and signed Git tag](https://www.git-scm.com/book/en/v2/Git-Basics-Tagging).
        -   List PRs and commits in the tag message:
            ```sh
            git log --pretty=format:"- %s (%h)" \
              "$(git describe --abbrev=0 --tags)"..HEAD
            ```
        -   Omit the leading `v` (use `1.0.0` instead of `v1.0.0`)
        -   Example: `git tag -a -s 1.0.0`
    -   Push the tag. GitHub Actions will build and push the Python package and Docker images, and open a PR to update the changelog.
    -   Squash and merge the changelog PR, removing any [`Co-authored-by` trailers](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors) before merging.
