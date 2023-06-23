import os
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()

env_file_path = ".env"

# API_KEYとAPI_SECRETの値を取得
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

if api_key and api_secret:
    # API_KEYとAPI_SECRETがすでに定義済みの場合
    print("API_KEYおよびAPI_SECRETは既に定義されています。")
else:
    # .envファイルの存在を確認
    if not os.path.exists(".env"):
        print(".envファイルは存在しません。")
        exit()

    # API_KEYの設定
    if not api_key:
        api_key = input("API_KEYを入力してください: ")

    # API_SECRETの設定
    if not api_secret:
        api_secret = input("API_SECRETを入力してください: ")
    
    # .envファイルの上書き
    with open(env_file_path, "w") as env_file:
        env_file.write(f"API_KEY={os.getenv('API_KEY')}\n")
        env_file.write(f"API_SECRET={os.getenv('API_SECRET')}\n")

    print(".envファイルの設定が完了しました。")
