# python-bitbankcc-ios-shortcuts
This repository is intended for handling the Public &amp; Private APIs of https://bitbank.cc/ using the python-bitbankcc library within iOS Shortcuts.

# 🚨 Notes
- This code does not necessarily guarantee that the expected data will be obtained.

- Please use this code at your own risk, as we are not responsible for any damages incurred by executing or referring to this code.

- This code executes a limit order, but the price specified depends on the minimum order quantity. Please note that if the specified order price is less than the minimum order quantity by calculation, the order volume may be less than the specified order price.

- This code is implemented based on bitbank's API specifications; API specifications are subject to change, so please check the latest information before using this code.

- This code is for the currency pair btc_jpy. Please note that other currency pairs have not been confirmed.

# Usage

## For Python virtualenv

> 🚨 **Note:**<br />
> **The following procedure requires a Python virtualenv (e.g., venv, pyenv-virtualenv) environment.**

### Execution grant

```
chmod +x setup_config.sh setup_for_pyenv_virtualenv.sh
```

### Install packages and build environment

```
./setup_for_pyenv_virtualenv.sh
```

### Order

Execute the following to place a limit order for btc_jpy at a specified price using bitbank API

```
cd src
python input_spot_order.py
```

## For poetry

> 🚨 **Note:**<br />
> **The following procedure requires the installation of poetry.**
> **For Poetry installation, [check the official website](https://python-poetry.org/docs/#installing-with-the-official-installer).**

### Execution grant

```
chmod +x setup_config.sh setup_for_poetry_venv.sh
```

### Install packages and build environment

Execute `poetry install --no-root` with the following shell script.

```
./setup_for_poetry_venv.sh
```

To install packages for the development environment, do the following

```
poetry install
```

### Order

Execute the following to place a limit order for btc_jpy at a specified price using bitbank API

```
cd src
python input_spot_order.py
```

## For iOS Shortcuts

To be filled in at a later date.