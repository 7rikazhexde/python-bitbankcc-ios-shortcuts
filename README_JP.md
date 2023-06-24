# python-bitbankcc-ios-shortcuts

このリポジトリは iOS Shortcuts 内で [python-bitbankcc ライブラリ](https://github.com/bitbankinc/python-bitbankcc)を使用して https://bitbank.cc/ の Public & Private API を扱うためのものです。

[English](./README.md) is here.

# 目次

- [python-bitbankcc-ios-shortcuts](#python-bitbankcc-ios-shortcuts)
- [目次](#%E7%9B%AE%E6%AC%A1)
- [🚨 注意事項](#-%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A0%85)
- [使い方](#%E4%BD%BF%E3%81%84%E6%96%B9)
  - [iOS Shortcutsアプリ向け](#ios-shortcuts%E3%82%A2%E3%83%97%E3%83%AA%E5%90%91%E3%81%91)
    - [1️⃣ 設定](#1%EF%B8%8F%E2%83%A3-%E8%A8%AD%E5%AE%9A)
      - [python-bitbankcc-ios-shortcuts setup](#python-bitbankcc-ios-shortcuts-setup)
    - [2️⃣ Spot order](#2%EF%B8%8F%E2%83%A3-spot-order)
      - [a-Shell bitbankAPI spot order](#a-shell-bitbankapi-spot-order)
  - [Python virtualenv向け](#python-virtualenv%E5%90%91%E3%81%91)
    - [1️⃣ プロジェクトのクローン](#1%EF%B8%8F%E2%83%A3-%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AE%E3%82%AF%E3%83%AD%E3%83%BC%E3%83%B3)
    - [2️⃣ 実行権限付与](#2%EF%B8%8F%E2%83%A3-%E5%AE%9F%E8%A1%8C%E6%A8%A9%E9%99%90%E4%BB%98%E4%B8%8E)
    - [3️⃣ パッケージのインストールとビルド環境の構築](#3%EF%B8%8F%E2%83%A3-%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E3%83%93%E3%83%AB%E3%83%89%E7%92%B0%E5%A2%83%E3%81%AE%E6%A7%8B%E7%AF%89)
    - [4️⃣ 指値注文](#4%EF%B8%8F%E2%83%A3-%E6%8C%87%E5%80%A4%E6%B3%A8%E6%96%87)
  - [poetry向け](#poetry%E5%90%91%E3%81%91)
    - [1️⃣ プロジェクトのクローン](#1%EF%B8%8F%E2%83%A3-%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AE%E3%82%AF%E3%83%AD%E3%83%BC%E3%83%B3-1)
    - [2️⃣ 実行権限付与](#2%EF%B8%8F%E2%83%A3-%E5%AE%9F%E8%A1%8C%E6%A8%A9%E9%99%90%E4%BB%98%E4%B8%8E-1)
    - [3️⃣ パッケージのインストールとビルド環境の構築](#3%EF%B8%8F%E2%83%A3-%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%A8%E3%83%93%E3%83%AB%E3%83%89%E7%92%B0%E5%A2%83%E3%81%AE%E6%A7%8B%E7%AF%89-1)
    - [4️⃣ 指値注文](#4%EF%B8%8F%E2%83%A3-%E6%8C%87%E5%80%A4%E6%B3%A8%E6%96%87-1)

# 🚨 注意事項

- このコードは必ずしも期待したデータが得られることを保証するものではありません。

- 本コードを実行または参照したことにより発生したいかなる損害についても責任を負いかねますので、自己責任でご利用ください。

- このコードは指値注文を実行しますが、指定される価格は最低注文数量によって異なります。指定された注文価格が計算上最小注文数量に満たない場合、注文数量が指定された注文価格を下回ることがありますのでご注意ください。

- 本コードはbitbankのAPI仕様に基づいて実装されています。API仕様は変更される可能性がありますので、ご利用の際は最新の情報をご確認ください。

- 本コードは通貨ペア btc_jpy を対象としています。他の通貨ペアは未確認ですのでご注意ください。

# 使い方

## iOS Shortcutsアプリ向け

> 🚨 **Note:**<br />
> **以下のショートカットはiPhoneとiPadにのみ対応しています。**
> **Mac/Windows/Linuxの場合は、以下の[For Python virtualenv](#for-python-virtualenv) または [For poetry](#for-poetry)を参照してください。**

### 1️⃣ 設定

iCloudのリンクから以下のショートカットを取得して実行すると、GitHubから[python-bitbankcc-ios-shortcuts](https://github.com/7rikazhexde/python-bitbankcc-ios-shortcuts)のソースコードを取得し、必要なパッケージをインストールすることができます。

#### python-bitbankcc-ios-shortcuts setup

https://www.icloud.com/shortcuts/24ea8d5558334dc1ba0c5b58e0bd0207

### 2️⃣ Spot order

iCloudのリンクから以下のショートカットを取得して実行すると、bitbankAPIを使用してbtc_jpyで指値注文を出すことができます。

#### a-Shell bitbankAPI spot order

https://www.icloud.com/shortcuts/16d3704ee5334ae9b68b75548fb0177e

> 🚨 **注意事項:**<br />
> このショートカットは、python-bitbankcc-ios-shortcuts セットアップショートカットが既に実行されていることを前提とします。
>
> `.env`ファイルでAPI_KEYとAPI_SECRETを設定する必要があります。(※1)\*\*
>
> `.env`はvimコマンドや他のアプリケーションから選択して変更してください。
>
> (※1)bitbankAPIの作成方法については、以下の公式情報をご確認ください。
>
> **https://support.bitbank.cc/hc/ja/articles/360036234574-APIキーの発行とAPI仕様の確認方法#h_62a68a59-b459-421e-8c18-335677d1a0a2**

## Python virtualenv向け

> 🚨 **注意事項:**<br />
> **以下の手順には、Pythonのvirtualenv（例：venv、pyenv-virtualenv）環境が必要です。**

### 1️⃣ プロジェクトのクローン

```bash
git clone https://github.com/7rikazhexde/python-bitbankcc-ios-shortcuts.git
```

### 2️⃣ 実行権限付与

```bash
chmod +x setup_config.sh setup_bbapi.sh
```

### 3️⃣ パッケージのインストールとビルド環境の構築

```bash
./setup_bbapi.sh
```

### 4️⃣ 指値注文

ビットバンクAPIを使用して、指定価格でbtc_jpyの指値注文を発注するために以下を実行します。

```bash
cd src
python input_spot_order.py
```

## poetry向け

> 🚨 **注意事項:**<br />
> **以下の手順は、poetryのインストールが必要です。**
> **poetryのインストールについては、[公式サイトをご確認ください](https://python-poetry.org/docs/#installing-with-the-official-installer)。**

### 1️⃣ プロジェクトのクローン

```bash
git clone https://github.com/7rikazhexde/python-bitbankcc-ios-shortcuts.git
```

### 2️⃣ 実行権限付与

```bash
chmod +x setup_config.sh setup_bbapi_for_poetry.sh
```

### 3️⃣ パッケージのインストールとビルド環境の構築

以下のシェルスクリプトで `poetry install --no-root` を実行する。

```bash
./setup_bbapi_for_poetry.sh
```

開発環境用のパッケージをインストールするには、以下を実行する。

```bash
poetry install
```

### 4️⃣ 指値注文

ビットバンクAPIを使用して、指定価格でbtc_jpyの指値注文を発注するために以下を実行します。

以下の指定では5000円分指値注文を出します。

```bash
cd src
python input_spot_order.py 5000
```
