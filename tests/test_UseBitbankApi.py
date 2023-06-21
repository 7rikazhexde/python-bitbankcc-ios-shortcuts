import os
import os.path
import sys

import pytest
from dotenv import load_dotenv
from pytest import MonkeyPatch

# テスト用のAPIキーとAPIシークレット
TEST_API_KEY = "test_api_key"
TEST_API_SECRET = "test_api_secret"

# ルートディレクトリのパスを取得
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# sys.pathにルートディレクトリを追加
sys.path.insert(0, ROOT_DIR)

from src.input_spot_order import UseBitbankApi


@pytest.fixture(autouse=True)
def load_env_vars(monkeypatch: MonkeyPatch) -> None:
    # 環境変数をテスト用の値で上書きする
    load_dotenv()
    monkeypatch.setenv("API_KEY", TEST_API_KEY)
    monkeypatch.setenv("API_SECRET", TEST_API_SECRET)


def test_UseBitbankApi_constructor(monkeypatch: MonkeyPatch) -> None:
    script_name: str = os.path.basename(sys.argv[0])
    monkeypatch.setattr("src.input_spot_order.sys.argv", [script_name])
    # コマンドライン引数が指定されていない場合のテスト
    obj = UseBitbankApi()
    assert obj._adjust_order_num == 500
    assert obj._api_key == TEST_API_KEY
    assert obj._api_secret == TEST_API_SECRET

    monkeypatch.setattr("src.input_spot_order.sys.argv", [script_name, "1000"])
    # コマンドライン引数が指定されている場合のテスト
    obj = UseBitbankApi()
    assert obj._adjust_order_num == 1000
    assert obj._api_key == TEST_API_KEY
    assert obj._api_secret == TEST_API_SECRET


def test_UseBitbankApi_constructor_invalid_args(monkeypatch: MonkeyPatch) -> None:
    script_name: str = os.path.basename(sys.argv[0])
    monkeypatch.setattr("src.input_spot_order.sys.argv", [script_name, "1000", "2000"])
    # コマンドライン引数が複数指定された場合のテスト
    with pytest.raises(ValueError) as exc_info:
        UseBitbankApi()

    assert str(exc_info.value) == "価格は一つのみ指定してください"


def test_get_ticker() -> None:
    obj = UseBitbankApi()
    ticker_ptn = "buy"
    pair = "btc_jpy"
    result = obj.get_ticker(ticker_ptn, pair)

    # タイムスタンプが整数値であることを検証
    assert isinstance(int(result), int)

    # タイムスタンプの範囲を検証（例として 0 から 5000000 の範囲）
    assert 0 <= int(result) <= 5000000


def test_set_order_data() -> None:
    obj = UseBitbankApi()
    ticker_ptn = "buy"
    pair = "btc_jpy"
    order_num, order_price = obj.set_order_data(ticker_ptn, pair)

    # 注文数量と注文価格が正しい値であることを検証
    assert isinstance(order_num, float)
    assert isinstance(order_price, int)

    # 注文数量がゼロより大きいことを検証
    assert order_num > 0

    # 注文価格がティッカー情報から調整パラメータを差し引いた値であることを検証
    assert order_price == int(obj.get_ticker(ticker_ptn, pair)) - obj._adjust_price


def test_spot_order() -> None:
    """指値注文時のresponse(型)を確認するテストコード

    Args:
        None

    Returns:
        None

    Note:
        - テストコードでは実際に注文を実行しますのでご注意ください。
        - テスト後はbitbankアプリから注文取消することを推奨します。
        - テスト時にはAPI_KEY_FOR_TEST,API_SEACRET_FOR_TESTを作成してください。
        - 値はそれぞれAPI_KEY,API_SECRETと同じで構いません。

    """
    load_dotenv()
    test_api_key = os.environ["API_KEY_FOR_TEST"]
    test_api_secret = os.environ["API_SECRET_FOR_TEST"]
    obj = UseBitbankApi(test_api_key, test_api_secret)
    ticker_ptn = "buy"
    pair = "btc_jpy"
    response = obj.spot_order(ticker_ptn, pair)

    # 必要なキーが存在することを検証
    assert "order_id" in response
    assert "pair" in response
    assert "side" in response
    assert "type" in response
    assert "start_amount" in response
    assert "remaining_amount" in response
    assert "executed_amount" in response
    assert "price" in response
    assert "average_price" in response
    assert "ordered_at" in response
    assert "status" in response
    assert "expire_at" in response
    assert "post_only" in response

    # キーの値が適切なデータ型であることを検証
    assert isinstance(response["order_id"], int)
    assert isinstance(response["pair"], str)
    assert isinstance(response["side"], str)
    assert isinstance(response["type"], str)
    assert isinstance(response["start_amount"], str)
    assert isinstance(response["remaining_amount"], str)
    assert isinstance(response["executed_amount"], str)
    assert isinstance(response["price"], str)
    assert isinstance(response["average_price"], str)
    assert isinstance(response["ordered_at"], int)
    assert isinstance(response["status"], str)
    assert isinstance(response["expire_at"], int)
    assert isinstance(response["post_only"], bool)


def test_conv_unixtime() -> None:
    use_bitbank_api = UseBitbankApi()
    unix_time = 1687271836560
    expected_local_time = "2023/06/20 23:37:16"

    local_time = use_bitbank_api.conv_unixtime(unix_time)

    assert local_time == expected_local_time


def test_file_write() -> None:
    use_bitbank_api = UseBitbankApi()
    data_to_write = "{'pair': 'btc_jpy', 'side': 'buy'}"
    file_path = "./response.txt"

    # ファイルが存在する場合は削除しておく
    if os.path.exists(file_path):
        os.remove(file_path)

    # ファイルを書き込む前にファイルが存在しないことを確認
    assert not os.path.exists(file_path)

    use_bitbank_api.file_write(data_to_write)

    # ファイルが正しく書き込まれたことを確認
    assert os.path.exists(file_path)

    with open(file_path, "r") as f:
        written_data = f.read()

    assert written_data == data_to_write

    # ファイルを削除
    os.remove(file_path)
