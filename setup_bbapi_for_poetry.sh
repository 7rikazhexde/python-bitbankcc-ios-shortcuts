#!/bin/bash

# poetry環境作成
# poetry.lock ファイルの存在を確認
if [[ -f "poetry.lock" ]]; then
    echo "poetry.lock found. Skipping 'poetry install --no-root'."
else
    echo "poetry.lock not found. Running 'poetry install --no-root'."
    poetry install --no-root
fi

# 設定ファイル作成
sh setup_config.sh
