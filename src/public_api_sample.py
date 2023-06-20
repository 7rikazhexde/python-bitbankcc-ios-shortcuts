import json

import python_bitbankcc

# public API classのオブジェクトを取得
pub = python_bitbankcc.public()

# PUBLIC TEST

value = pub.get_ticker("btc_jpy")  # ペア
print(json.dumps(value))

value = pub.get_depth("btc_jpy")  # ペア
print(json.dumps(value))

value = pub.get_transactions("btc_jpy")  # ペア
print(json.dumps(value))

# 同じメソッドを日にち指定で
value = pub.get_transactions("btc_jpy", "20230101")  # ペア  # YYYYMMDD 型の日付
print(json.dumps(value))

value = pub.get_candlestick(
    "btc_jpy", "1hour", "20230101"  # ペア  # タイプ  # YYYYMMDD 型の日付
)
print(json.dumps(value))
