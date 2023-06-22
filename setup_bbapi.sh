#!/bin/bash

# venvかpyenv-virtualenvで仮想環境を作成してください。

# リポジトリをクローン
# git clone https://github.com/bitbankinc/python-bitbankcc.git

# クローンしたリポジトリのディレクトリに移動
# cd python-bitbankcc

# 最新のコミットに切り替え
# git checkout HEAD

# パッケージをインストール
pip install git+https://github.com/bitbankinc/python-bitbankcc#egg=python-bitbankcc
pip install python-dotenv
pip install requests

# 一つ上のディレクトリに移動
# cd ..

# 設定ファイル作成
sh ./setup_config.sh

# python-bitbankccフォルダを削除
# rm -rf python-bitbankcc
