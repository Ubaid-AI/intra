# Intra

For Intra Customization

## Directory Structure

### Root Directory

- `.editorconfig` - Editor configuration for consistent coding styles
- `.eslintrc` - ESLint configuration for JavaScript code quality
- `.github/` - GitHub workflows and CI/CD configurations
- `.gitignore` - Specifies files to be ignored by Git
- `.pre-commit-config.yaml` - Pre-commit hook configurations
- `license.txt` - License information for the application
- `pyproject.toml` - Python project configuration and dependencies
- `README.md` - This documentation file

### Main Application (`intra/`)

The main application code is organized in the `intra/` directory with the following structure:

#### Core Files

- `__init__.py` - Python package initialization
- `hooks.py` - Frappe framework hooks for extending functionality
- `install.py` - Installation procedures
- `uninstall.py` - Uninstallation procedures
- `modules.txt` - Module declarations
- `patches.txt` - Database and code migration patches

#### Configuration (`intra/config/`)

- Contains configuration settings for the application

#### Application Modules (`intra/intra/`)

- Contains application-specific modules and business logic

#### Public Assets (`intra/public/`)

- `css/` - Stylesheets including `intra.css`
- `images/` - Application images including:
  - `favicon.png` - Browser favicon
  - `logo.png` - Application logo
  - `splash.png` - Splash screen image

#### Templates (`intra/templates/`)

- `pages/` - Page templates for rendering views

#### Workspace (`intra/workspace/`)

- `erpnextrename/` - Workspace configurations for ERPNext integration
  - `erpnextrename.json` - ERPNext workspace configuration

## Important Configuration Files

- `hooks.py` - Defines integration points with the Frappe framework
- `pyproject.toml` - Python project dependencies and build settings
- `modules.txt` - Declares modules to be loaded by the application
- `patches.txt` - Lists database migrations and code patches

## Navigation Guide for Developers

### Getting Started

1. Begin by exploring the `hooks.py` file to understand how the application integrates with Frappe
2. Review the module structure in `modules.txt`
3. Examine the application-specific code in the `intra/intra/` directory

### Making UI Changes

1. CSS modifications should be made in `intra/public/css/intra.css`
2. Images are stored in `intra/public/images/`
3. Page templates can be found in `intra/templates/pages/`

### Adding New Features

1. Create appropriate modules in the `intra/intra/` directory
2. Update `hooks.py` to register new functionality with the Frappe framework
3. Add any necessary database migrations to `patches.txt`

### Workspace Customizations

1. Workspace configurations are stored in `intra/workspace/erpnextrename/`
2. Modify `erpnextrename.json` to adjust the ERPNext workspace integration

## Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app intra
```

## Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/intra
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

## CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.

## License

mit
