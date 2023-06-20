#!/bin/bash

# 環境変数用ファイルを作成
if [[ -f ".env" ]]; then
    echo ".env found. Skipping 'touch .env'."
else
    echo ".env not found. Running 'touch .env'."
    touch .env
fi

# 結果出力用ファイル作成
if [[ -f "response.txt" ]]; then
    echo "response.txt found. Skipping 'touch response.txt'."
else
    echo "response.txt not found. Running 'touch response.txt'."
    touch response.txt
fi

