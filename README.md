# MLOps_kasmakoli
Machine Learning Operations 02476

## Environment Setup

This project uses [UV](https://github.com/astral-sh/uv) for fast Python package management and virtual environment handling.

### Initial Setup

The virtual environment has already been created. To activate it:

```bash
source .venv/bin/activate
```

### Installing Packages

To add a new package to the project:

```bash
uv pip install <package-name>
```

Or add it to `pyproject.toml` dependencies and sync:

```bash
uv sync
```

### Managing Dependencies

- **Add a package**: `uv pip install <package-name>`
- **Remove a package**: `uv pip uninstall <package-name>`
- **List installed packages**: `uv pip list`
- **Sync dependencies**: `uv sync` (installs all packages from pyproject.toml)

### Python Version

The project uses Python 3.11 (specified in `.python-version`).
