# Python Data Structures and Algorithms

[![CI](https://github.com/ahcodedev/python-ds-algorithms/actions/workflows/python.yml/badge.svg?branch=main)](https://github.com/ahcodedev/python-ds-algorithms/actions/workflows/python.yml)
[![Security](https://github.com/ahcodedev/python-ds-algorithms/actions/workflows/security.yml/badge.svg?branch=main)](https://github.com/ahcodedev/python-ds-algorithms/actions/workflows/security.yml)
[![gitleaks](https://img.shields.io/badge/protected%20by-gitleaks-blue)](https://github.com/gitleaks/gitleaks)

Various Data Structures and Algorithm Solutions in Python (3.x). Succinct Python one-liners are avoided in most solutions
to prevent obscuring the function and logic of the algorithms / data-structures.

* [Algorithm Theory](src/algorithm_theory/)
* [Data Structures](src/data_structures/)

## Algorithms

* [Arrays](src/arrays/)
* [Binary Search](src/binary_search/)
* [Binary Tree](src/binary_tree/)
* [Circularly Linked Lists](src/circularly_linked_list/)
* [Doubly Linked Lists](src/doubly_linked_list/)
* [Integers](src/integers/)
* [Math Problems](src/math_problems/)
* [Matrices](src/multi_dimensional_arrays/)
* [N-ary Tree](src/n_ary_tree/)
* [Queues](src/queues/)
* [Singly Linked Lists](src/singly_linked_lists/)
* [Stacks](src/stacks/)
* [Strings](src/strings/)
* [Trie](src/trie/)

Each directory's problems and approaches are documented as doc comments directly in the corresponding `.py` files.

## Setup

Project supports local development and VSCode Dev container development

### Local Development Installation

Note: Project uses `uv` and `just` to
manage project configuration and commands

* Install tools and sync the project - `just setup` (runs `brew bundle install`, then `just sync`)

### VS Code Dev Container

* Install Docker
* Install VSCode
* Open project folder in VS Code
* Install recommended extensions
* Reopen in container using Remote Development Container menu

## Project Commands

* `just setup` - install Homebrew tools from the `Brewfile` and sync the project
* `just sync` - sync project dependencies (all groups)
* `just lint` - type check, lint, format, spellcheck, and lint workflows (actionlint) (applies fixes)
* `just ci-lint` - run the same checks without modifying files (used in CI)
* `just test` - run unit tests
* `just audit` - check dependencies for known vulnerabilities with pip-audit
* `just markdownlint` - lint Markdown files with markdownlint-cli2
* `just prek` - run pre-commit hooks via prek
* `just git-leaks` - scan staged changes for secrets with gitleaks
* `just zizmor` - audit GitHub Actions workflows for security issues
* `uv add {package}` - install a dependency

## CI and Security

| Workflow              | Runs on                 | Purpose                                      |
| --------------------- | ----------------------- | -------------------------------------------- |
| `python.yml`          | push / PR to `main`     | lint, unit tests, markdownlint               |
| `security.yml`        | push to `main`, all PRs | zizmor, gitleaks, pip-audit dependency audit |

* GitHub Actions are pinned to full commit SHAs, with the version in a trailing comment
* Dependabot (`.github/dependabot.yml`) checks monthly for updates to GitHub Actions, Python
  dependencies, the dev container image, and dev container features. New releases wait 7 days
  before an update is proposed. Dependabot PRs get the `dependencies` label
