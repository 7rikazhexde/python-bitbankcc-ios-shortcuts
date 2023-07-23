import os

# .envファイルが存在しない場合のみ追記する
if not os.path.isfile(".env"):
    print(".env not found. Running creation.")
    with open(".env", "w") as env_file:
        env_file.write("API_KEY=\n")
        env_file.write("API_SECRET=\n")
else:
    print(".env found. Skipping creation.")

# 結果出力用ファイル作成
if os.path.isfile("./src/response.txt"):
    print("response.txt found. Skipping creation.")
else:
    print("response.txt not found. Running creation.")
    with open("./src/response.txt", "w"):
        pass
