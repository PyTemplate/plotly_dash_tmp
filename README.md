```bash

   ___        _____                         _         _
  / _ \ _   _/__   \ ___  _ __ ___   _ __  | |  __ _ | |_  ___  ___
 / /_)/| | | | / /\// _ \| '_ ` _ \ | '_ \ | | / _` || __|/ _ \/ __|
/ ___/ | |_| |/ /  |  __/| | | | | || |_) || || (_| || |_|  __/\__ \
\/      \__, |\/    \___||_| |_| |_|| .__/ |_| \__,_| \__|\___||___/
        |___/                       |_|

```
<!-- source - https://patorjk.com/software/taag/#p=display&h=1&f=Ogre&t=PyTemplates -->

[![License](https://img.shields.io/badge/License-Creative%20Commons%20Zero%20v1.0-informational?style=flat)](./LICENSE)
[![Documentation: Sphinx](https://img.shields.io/badge/Documentation-Sphinx-08476D?style=flat)](https://www.sphinx-doc.org/en/master/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-151515?style=flat)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/crabtr26/pytemplates/branch/main/graph/badge.svg?token=RRYTJVFDG3)](https://codecov.io/gh/crabtr26/pytemplates)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/crabtr26/pytemplates/main.svg)](https://results.pre-commit.ci/latest/github/crabtr26/pytemplates/main)
<!-- [![Imports: isort](https://img.shields.io/badge/%20imports-isort-EE8236?style=flat)](https://pycqa.github.io/isort/) -->

## Description

A basic plotly dashboard template which includes proper package structure with a functioning package installation.
The package is built using poetry; metadata and dependency information is stored in the pyproject.toml.
This template includes flake8, pylint, isort, and pytest settings with configurations compatible with
the black autoformatter. Pylint settings are based on the Google style standards for python
and adapted for black compatibility.  Testing is automated using github workflows, codecov.io,
and pre-commit.ci. Application deployment is managed using multi-staged docker builds for fast develop/deploy
cycles.

**Demo Available at -** https://pytemplates.gallery/

## Basic Setup

Using `poetry`:

```bash
git clone https://github.com/crabtr26/pytemplates.git
cd pytemplates
poetry install --no-dev
poetry shell
gunicorn pytemplates.main:server
```

## Development Setup

Using `poetry`:

```bash
git clone https://github.com/crabtr26/pytemplates.git
cd pytemplates
poetry install
poetry shell
gunicorn pytemplates.main:server
```

Using `Docker`:

```bash
git clone https://github.com/crabtr26/pytemplates.git
cd pytemplates
docker build . -t plotly_dash
docker run --rm -p 3000:80 plotly_dash
```

## Testing

To run the unit tests locally using the development environment:

```bash
cd pytemplates
poetry run pytest
```

## Documentation

To build and view the documentation locally using the development environment:

```bash
cd pytemplates/docs
make html
google-chrome build/html/index.html
```
