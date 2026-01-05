# MLOps_kasmakoli
Machine Learning Operations 02476

## Quick Setup: Create `uvr` Alias

For easier use, create an alias for `uv run`:

```bash
nano ~/.zshrc
```

Tilføj aller nederst: `alias uvr='uv run'`

Save: `ctrl+O`, `Enter`, `ctrl+X`

Test: `uvr --help`

Hvis der kommer noget legit -> lezz go

## Environment Setup

We [UV](https://github.com/astral-sh/uv) as per instructed by SkafteNicki. UV uses a project-based approach, which means all operations are done within this project folder.

### Running Scripts

To run a script using the virtual environment:

```bash
uvr script.py
```

You can think of `uvr` as equivalent to `python` inside the virtual environment.
NB! if you haven't added the alias to your `~/.zshrc` then use `uv run` insteand of `uvr`.

### Activating the Virtual Environment (Optional)

Instead of using `uv run` every time, you can activate the virtual environment:

```bash
source .venv/bin/activate
```

After activation, you can use `python` and `pip` commands directly.

### Managing Dependencies

**Recommended approach (project-based):**

- **Add a package**: `uv add <package-name>` (adds to `pyproject.toml` and installs)
- **Add multiple packages**: `uv add numpy pandas`
- **Add development dependencies**: `uv add --dev pytest black`
- **Add optional dependencies**: `uv add --optional <package-name>`
- **Remove a package**: `uv remove <package-name>`
- **List installed packages**: `uv pip list`
- **Sync dependencies**: `uv sync` (installs all packages from `pyproject.toml`)

**Alternative approach (manual):**

You can also manually edit `pyproject.toml` to add dependencies, then run:

```bash
uv sync
```

### Project Files

- **`pyproject.toml`**: Contains project metadata and dependencies
- **`uv.lock`**: Lock file that ensures reproducible installs (auto-generated, do not edit manually)
- **`.venv/`**: Virtual environment directory (auto-created)

### Python Version

The project uses Python 3.13 (specified in `pyproject.toml`).
