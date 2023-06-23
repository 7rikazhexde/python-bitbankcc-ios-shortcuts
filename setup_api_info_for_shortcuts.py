import sys
import os
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()

# 引数の取得
api_key = sys.argv[1]
api_secret = sys.argv[2]

# .envファイルの設定
env_file_path = ".env"

# API_KEYの設定
if api_key:
    os.environ["API_KEY"] = api_key

# API_SECRETの設定
if api_secret:
    os.environ["API_SECRET"] = api_secret

# .envファイルの上書き
with open(env_file_path, "w") as env_file:
    env_file.write(f"API_KEY={os.getenv('API_KEY')}\n")
    env_file.write(f"API_SECRET={os.getenv('API_SECRET')}\n")

# 結果の表示
print(".envファイルの設定が完了しました。")
