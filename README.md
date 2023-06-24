# python-bitbankcc-ios-shortcuts

This repository is intended for handling the Public & Private APIs of https://bitbank.cc/ using the [python-bitbankcc](https://github.com/bitbankinc/python-bitbankcc) within iOS Shortcuts.

[日本語](./README_JP.md)はこちら。

# Table of Contents

- [python-bitbankcc-ios-shortcuts](#python-bitbankcc-ios-shortcuts)
- [Table of Contents](#table-of-contents)
- [🚨 Notes](#-notes)
- [Usage](#usage)
  - [For iOS Shortcuts App](#for-ios-shortcuts-app)
    - [1️⃣ setup](#1%EF%B8%8F%E2%83%A3-setup)
      - [python-bitbankcc-ios-shortcuts setup](#python-bitbankcc-ios-shortcuts-setup)
    - [2️⃣ Spot order](#2%EF%B8%8F%E2%83%A3-spot-order)
      - [a-Shell bitbankAPI spot order](#a-shell-bitbankapi-spot-order)
  - [For Python virtualenv](#for-python-virtualenv)
    - [1️⃣ project clone](#1%EF%B8%8F%E2%83%A3-project-clone)
    - [2️⃣ Execution grant](#2%EF%B8%8F%E2%83%A3-execution-grant)
    - [3️⃣ Install packages and build environment](#3%EF%B8%8F%E2%83%A3-install-packages-and-build-environment)
    - [Spot order](#spot-order)
  - [For poetry](#for-poetry)
    - [1️⃣ project clone](#1%EF%B8%8F%E2%83%A3-project-clone-1)
    - [2️⃣ Execution grant](#2%EF%B8%8F%E2%83%A3-execution-grant-1)
    - [3️⃣ Install packages and build environment](#3%EF%B8%8F%E2%83%A3-install-packages-and-build-environment-1)
    - [4️⃣ Spot order](#4%EF%B8%8F%E2%83%A3-spot-order)

# 🚨 Notes

- This code does not necessarily guarantee that the expected data will be obtained.

- Please use this code at your own risk, as I'm not responsible for any damages incurred by executing or referring to this code.

- This code executes a limit order, but the price specified depends on the minimum order quantity. Please note that if the specified order price is less than the minimum order quantity by calculation, the order volume may be less than the specified order price.

- This code is implemented based on bitbank's API specifications; API specifications are subject to change, so please check the latest information before using this code.

- This code is for the currency pair btc_jpy. Please note that other currency pairs have not been confirmed.

# Usage

## For iOS Shortcuts App

> 🚨 **Note:**<br />
> **The following shortcuts are for iPhone and iPad only; for Mac/Windows/Linux, see [For Python virtualenv](#for-python-virtualenv) or [For poetry](#for-poetry) below.**

### 1️⃣ setup

The following shortcut can be obtained from the iCloud link and run to obtain the source code for [python-bitbankcc-ios-shortcuts](https://github.com/7rikazhexde/python-bitbankcc-ios-shortcuts) from GitHub and install the necessary packages.

#### python-bitbankcc-ios-shortcuts setup

https://www.icloud.com/shortcuts/24ea8d5558334dc1ba0c5b58e0bd0207

### 2️⃣ Spot order

If you obtain and execute the following shortcut from the iCloud link, you can place a limit order with btc_jpy using bitbankAPI.

#### a-Shell bitbankAPI spot order

https://www.icloud.com/shortcuts/16d3704ee5334ae9b68b75548fb0177e

> 🚨 **Note:**<br />
> **This shortcut assumes that the python-bitbankcc-ios-shortcuts setup shortcut has already been executed.**
>
> **API_KEY and API_SECRET must be set in the `.env` file. (※1)**
>
> **Please select and change the `.env` from the vim command or other applications.**
>
> **(※1)Please check the following official information on how to create bitbankAPI.**
>
> **https://support.bitbank.cc/hc/ja/articles/360036234574-APIキーの発行とAPI仕様の確認方法#h_62a68a59-b459-421e-8c18-335677d1a0a2**

## For Python virtualenv

> 🚨 **Note:**<br />
> **The following procedure requires a Python virtualenv (e.g., venv, pyenv-virtualenv) environment.**

### 1️⃣ project clone

```bash
git clone https://github.com/7rikazhexde/python-bitbankcc-ios-shortcuts.git
```

### 2️⃣ Execution grant

```bash
chmod +x setup_config.sh setup_bbapi.sh
```

### 3️⃣ Install packages and build environment

```bash
./setup_bbapi.sh
```

### Spot order

Execute the following to place a limit order for btc_jpy at a specified price using bitbank API

```bash
cd src
python input_spot_order.py
```

## For poetry

> 🚨 **Note:**<br />
> **The following procedure requires the installation of poetry.**
> **For Poetry installation, [check the official website](https://python-poetry.org/docs/#installing-with-the-official-installer).**

### 1️⃣ project clone

```bash
git clone https://github.com/7rikazhexde/python-bitbankcc-ios-shortcuts.git
```

### 2️⃣ Execution grant

```bash
chmod +x setup_config.sh setup_bbapi_for_poetry.sh
```

### 3️⃣ Install packages and build environment

Execute `poetry install --no-root` with the following shell script.

```bash
./setup_bbapi_for_poetry.sh
```

To install packages for the development environment, do the following

```bash
poetry install
```

### 4️⃣ Spot order

Execute the following to place a limit order for btc_jpy at a specified price using bitbank API

The following designation places a limit order for 5,000 JPY yen.

```bash
cd src
python input_spot_order.py 5000
```
