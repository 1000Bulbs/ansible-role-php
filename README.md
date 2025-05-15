# Ansible Role: php

[![CI](https://github.com/1000Bulbs/ansible-role-php/actions/workflows/ci.yml/badge.svg)](https://github.com/1000Bulbs/ansible-role-php/actions/workflows/ci.yml)

This Ansible role installs and configures PHP on Debian-based systems. It manages PHP repository setup, installs PHP and extensions, configures INI files for different SAPIs (CLI, Apache2), installs and enables the geoip extension via PECL, and ensures required dependencies and configuration files are present.

---

## ✅ Requirements

- Ansible 2.13+
- Python 3.9+ (for Molecule + testinfra)
- Tested on Ubuntu 22.04+

---

## ⚙️ Role Variables

These variables can be overridden in your inventory, playbooks, or `group_vars`.

### Defaults (`defaults/main.yml`)

- `php_version`: The PHP version to install (e.g., `8.1`).
- `php_base_packages`: List of base PHP packages to install.
- `php_extensions`: List of PHP extensions to install.
- `php_ini_sapi_configs`: List of SAPI-specific PHP INI configuration options.

### Variables (`vars/main.yml`)

- `php_ppa_dependencies`: List of packages required to add the PHP PPA.
- `php_repo`: The PPA repository to use (default: `ondrej/php`).
- `php_source_list_file`: Path to the PHP PPA source list file.
- `php_phing_file`: Destination path for the phing file.

---

## 📦 Dependencies

This role has no external dependencies.

---

## 📥 Installing the Role

To include this role in your project using a `requirements.yml` file:

```yaml
roles:
  - name: okb.php
    src: git@github.com:1000bulbs/ansible-role-php.git
    scm: git
    version: master
```

Then install it with:

```bash
ansible-galaxy role install -r requirements.yml
```

---

## 💡 Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for
users too:

```yaml
- name: My Playbook
  hosts: all
  become: true
  roles:
    - role: okb.php
```

---

## 🧪 Testing

This role uses a `Makefile` for linting and formatting, and [Molecule](https://molecule.readthedocs.io/) with
`pytest-testinfra` for integration testing.

### Run tests locally

#### Lint and Format

```bash
# Run all checks (linting and formatting)
make check

# Run linting tools manually (ruff, yamllint, ansible-lint)
make lint

# Run Python formatting tools manually (ruff)

make format
```

#### Integration Tests

Install dependencies

```bash
pip install -r requirements.txt
```

Run Molecule integration tests

```bash
molecule test
```

---

## 🪝 Git Hooks

This project includes [pre-commit](https://pre-commit.com/) integration via Git hooks to automatically run formatting and linting checks **before each commit**.

These hooks help catch errors early and keep the codebase consistent across contributors.

### Install Git Hooks

```bash
make install-hooks
```

This will:

- Install pre-commit (if not already installed)
- Register a Git hook in .git/hooks/pre-commit
- Automatically run checks like:
- Code formatting with black and isort
- Linting with ruff, yamllint, and ansible-lint

### Remove Git Hooks

```bash
make uninstall-hooks
```

This removes the Git pre-commit hook and disables automatic checks.

💡 Even with hooks uninstalled, you can still run the same checks manually with `make test`.

Why Use Git Hooks?

- Ensures consistency across contributors
- Catches syntax and style issues before they hit CI
- Prevents accidental commits of broken or misformatted files
- Integrates seamlessly with your local workflow
