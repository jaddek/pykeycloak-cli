# Release Guide

This project already has GitHub Actions publish flow on release tags (`vX.Y.Z`).
Use this guide for safe local verification and release prep.

## One-Time Setup

- Create PyPI project and API token:
  - `PYPI_API_TOKEN` for production publishes.
- (Optional) Create TestPyPI token for dry runs.
- If using GitHub Actions publish:
  - Add repository secret `PYPI_API_TOKEN`.
- If publishing locally with `twine`:
  - export credentials:
    - `TWINE_USERNAME=__token__`
    - `TWINE_PASSWORD=<pypi-or-testpypi-token>`

## Pre-Release Checklist

1. Ensure dependency lock and sources are correct:
   - `uv sync --dev`
2. Run quality gates:
   - `make lint`
   - `make typecheck`
   - `make test-with-coverage`
3. Verify package metadata:
   - project name/version/description in `pyproject.toml`
   - README renders correctly
4. Build and validate artifacts:
   - `make build-package`
   - `make check-package`
5. (Recommended) Install built wheel in a clean env and smoke test:
   - `python -m venv /tmp/pykc-smoke`
   - `source /tmp/pykc-smoke/bin/activate`
   - `pip install dist/*.whl`
   - `pykc.py --help` (or your installed console entry point)

## TestPyPI Dry Run (Recommended)

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=<testpypi-token>
make publish-testpypi
```

Then verify install from TestPyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple pykeycloak-cli==<version>
```

## Production Release via Tag (Recommended)

The CI workflow publishes on `v*` tags.

```bash
git checkout main
git pull
git tag vX.Y.Z
git push origin vX.Y.Z
```

What happens in CI:
- checks (`ruff`, `ty`, `pytest`, `pip-audit`)
- build (`uv build`)
- publish to PyPI
- GitHub Release creation

## Production Release with Git Flow

If your team uses Git Flow, release from `release/X.Y.Z` and let CI publish on tag.

```bash
git checkout develop
git pull
git flow release start X.Y.Z
```

On the release branch:

```bash
make release-bump-tag TAG=vX.Y.Z
git add pyproject.toml
git commit -m "chore(release): bump version to X.Y.Z"
make lint
make typecheck
make test-with-coverage
make build-package
make check-package
```

Finish release (creates merge commits and tag):

```bash
git flow release finish X.Y.Z
git push --follow-tags origin main develop
```

Notes:
- Your CI publish job is triggered by tags matching `v*`, so ensure the final tag is exactly `vX.Y.Z`.
- If Git Flow creates a lightweight/non-standard tag format, recreate it as annotated `vX.Y.Z` before pushing.
- If your default Git Flow branch names differ (`master` vs `main`), adapt the push command accordingly.

## Manual Production Publish (Fallback)

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=<pypi-token>
make publish-pypi
```

## Post-Release Verification

1. Install from PyPI:
   - `pipx install pykeycloak-cli==X.Y.Z` (or `pip install ...`)
2. Run:
   - `pykc.py --help`
3. Confirm release page and artifact availability.
