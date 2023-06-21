#!/bin/bash

# .envファイルが存在しない場合のみ追記する
if [[ ! -f ".env" ]]; then
    echo ".env not found. Running creation."
    echo "API_KEY=" > .env
    echo "API_SECRET=" >> .env
else
    echo ".env found. Skipping creation."
fi

# 結果出力用ファイル作成
if [[ -f "response.txt" ]]; then
    echo "response.txt found. Skipping creation"
else
    echo "response.txt not found. Running creation."
    touch response.txt
fi
