# Ansible Role: php

[![CI](https://github.com/1000Bulbs/ansible-role-php/actions/workflows/ci.yml/badge.svg)](https://github.com/1000Bulbs/ansible-role-php/actions/workflows/ci.yml)

This Ansible role installs and configures PHP on Debian-based systems. It manages PHP repository setup, installs PHP and extensions, configures INI files for different SAPIs (cli & fpm),and ensures required dependencies and configuration files are present.

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
    src: https://github.com/1000bulbs/ansible-role-php.git
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

This role uses Python and Node.js for linting and formatting, Molecule with pytest-testinfra for integration testing,
and Act for local GitHub Actions testing — all orchestrated through a Makefile for ease of use and convenience.

### Install dependencies

Install all dependencies and setup environment

```bash
make setup
```

### Run tests locally

#### Lint and Format Checks

Run lint and format checks

```bash
make check
```

#### Integration Tests

Run integration tests

```bash
make test
```

#### GitHub Actions Tests

Run github actions tests locally

```bash
make ci
```

---

## 🪝 Git Hooks

This project includes [pre-commit](https://pre-commit.com/) integration via Git hooks to automatically run formatting and linting checks **before each commit**.

These hooks help catch errors early and keep the codebase consistent across contributors.

### Prerequisites

Before installing the hooks, make sure your system has:

- **Python 3.9+** with `pip` installed
- **Node.js** and `npm` (required for `markdownlint-cli2`)

You can check your versions with:

```bash
python3 --version
pip --version
node --version
npm --version
```

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

### Test Git Hooks

```bash
make test-hooks
```

This will run the pre-commit hooks on all files, the same as when you run `git commit`.

### Remove Git Hooks

```bash
make uninstall-hooks
```

This removes the Git pre-commit hook and disables automatic checks.

💡 Even with hooks uninstalled, you can still run the same checks manually with `make test-hooks`.

Why Use Git Hooks?

- Ensures consistency across contributors
- Catches syntax and style issues before they hit CI
- Prevents accidental commits of broken or misformatted files
- Integrates seamlessly with your local workflow
