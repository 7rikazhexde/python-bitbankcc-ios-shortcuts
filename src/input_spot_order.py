import datetime
import json
import os
import sys
from typing import Dict, List, Optional, Tuple, Union

from dotenv import load_dotenv
from python_bitbankcc import private, public


class UseBitbankApi:
    def __init__(
        self, api_key: Optional[str] = None, api_secret: Optional[str] = None
    ) -> None:
        """UseBitbankApiのインスタンスを初期化します。

        publicクラスとprivateクラスのインスタンスを作成する
        価格指定する場合はコマンドライン引数で指定する

        Args:
            None

        Raises:
            ValueError: コマンドライン引数の数が無効な場合

        Returns:
            None

        Note:
            - コマンドライン引数を指定しない場合、`adjust_order_num`のデフォルト値が使用されます。
            - コマンドライン引数として指定すべき価格は1つだけです。
            - コマンドライン引数の数が無効な場合、プログラムは終了します。
            - privateクラスのインスタンス生成にはAPIキー情報が必要です。.envにAPI_KEYとAPI_SEACRETを指定してください。

        """
        self._args: List[str] = sys.argv
        if len(self._args) == 1:
            self._adjust_order_num: int = 500
        elif len(self._args) > 2:
            raise ValueError("価格は一つのみ指定してください")
        else:
            self._adjust_order_num = int(self._args[1])

        self._adjust_price: int = 0
        self._decimal_digits_btc: int = 8

        if api_key is not None and api_secret is not None:
            self._api_key = api_key
            self._api_secret = api_secret
        else:
            load_dotenv()
            self._api_key = os.environ["API_KEY"]
            self._api_secret = os.environ["API_SECRET"]

        if not self._api_key or not self._api_secret:
            raise FileNotFoundError(
                "API_KEY or API_SECRET is missing in the environment variables"
            )

        self._pub: public = public()

        self._prv: private = private(self._api_key, self._api_secret)

    def get_ticker(self, ticker_ptn: str, pair: str) -> str:
        """指定したペア、パターンのティッカー情報を取得する。

        指定されたペアとパターンのティッカー情報をビットバンクAPIから取得するメソッドです。

        Args:
            ticker_ptn (str): 取得するティッカーパターン (e.g., "buy", "sell", "high", "low", etc.).
            pair (str): ティッカー情報取得の対象となる取引ペア (e.g., "btc_jpy", "eth_jpy", etc.).

        Returns:
            str: 指定されたパターン、ペアに対応するティッカー値です.

        References:
            - ビットバンクAPIドキュメント(Ticker): https://github.com/bitbankinc/bitbank-api-docs/blob/master/public-api_JP.md#ticker

        """
        value = self._pub.get_ticker(pair)
        return value[ticker_ptn]

    def set_order_data(self, ticker_ptn: str, pair: str) -> Tuple[float, float]:
        """注文データを設定する。

        ティッカー情報と調整パラメータから注文数量と注文価格を計算して設定します。

        Args:
            ticker_ptn (str): 取得するティッカーパターン (e.g., "buy", "sell", "high", "low", etc.).
            pair (str): ティッカー情報取得の対象となる取引ペア (e.g., "btc_jpy", "eth_jpy", etc.).

        Returns:
            Tuple[float, float]: 計算された注文数量と注文価格のタプル。

        Raises:
            ValueError: 注文数量の計算中にエラーが発生した場合。

        Example:
            >>> use_bitbank_api = UseBitbankApi()
            >>> order_num, order_price = use_bitbank_api.set_order_data("buy", "btc_jpy")
            >>> print(order_num, order_price)
            (0.001, 3786040)

        Notes:
            - 注文数量は調整パラメータとティッカー情報から計算されます。
            - 注文価格はティッカー情報から調整パラメータを差し引いた値です。

        """
        buy_price = int(self.get_ticker(ticker_ptn, pair))
        order_num = self._adjust_order_num / (buy_price - self._adjust_price)
        order_num = round(order_num, self._decimal_digits_btc)
        order_price = buy_price - self._adjust_price
        return order_num, order_price

    def spot_order(self, ticker_ptn: str, pair: str) -> Dict[str, Union[int, str]]:
        """スポット注文を実行する。

        指定されたティッカーパターンと取引ペアに基づいてスポット注文を実行します。

        Args:
            ticker_ptn (str): 注文のティッカーパターン (e.g., "buy", "sell", "high", "low", etc.).
            pair (str): 注文の対象となる取引ペア (e.g., "btc_jpy", "eth_jpy", etc.).

        Returns:
            Dict[str, Union[int, str]]: 注文実行結果の辞書データ。注文情報やステータスが含まれます。

        Raises:
            ValueError: 注文の実行中にエラーが発生した場合。

        Example:
            >>> use_bitbank_api = UseBitbankApi()
            >>> response = use_bitbank_api.spot_order("buy", "btc_jpy")
            >>> print(response)
            {
                'order_id': 29465905899,
                'pair': 'btc_jpy',
                'side': 'buy',
                'type': 'limit',
                'start_amount': '0.0001',
                'remaining_amount': '0.0001',
                'executed_amount': '0.0000',
                'price': '3786540',
                'average_price': '0',
                'ordered_at': 1687271836560,
                'status': 'UNFILLED',
                'expire_at': 1702823836560,
                'post_only': False
            }

        Notes:
            - 注文はティッカーパターンと取引ペアに基づいて行われます。
            - 注文の実行結果は辞書形式で返されます。
            - 注文情報やステータスなど、注文に関する詳細が含まれます。
            - 指値注文ではPost Only指定で注文します。

        """
        order_num, order_price = self.set_order_data(ticker_ptn, pair)
        response = self._prv.order(
            pair, str(order_price), str(order_num), ticker_ptn, "limit", False, False
        )
        return response

    def conv_unixtime(self, unixtime: int) -> str:
        """Unix時間をローカル時間に変換する。

        指定されたUnix時間をミリ秒単位で受け取り、それをローカル時間に変換します。

        Args:
            unixtime (int): 変換するUnix時間（ミリ秒単位）。

        Returns:
            str: ローカル時間に変換された日時文字列（"YYYY/MM/DD HH:MM:SS" 形式）。

        Example:
            >>> use_bitbank_api = UseBitbankApi()
            >>> unix_time = 1687271836560
            >>> local_time = use_bitbank_api.conv_unixtime(unix_time)
            >>> print(local_time)
            "2023/06/20 23:12:30"

        Notes:
            - Unix時間はエポックからの経過時間をミリ秒で表現したものです。
            - このメソッドは指定されたUnix時間をローカル時間に変換します。
            - ローカル時間のフォーマットは "YYYY/MM/DD HH:MM:SS" です。

        """
        data = unixtime / 1000
        dt = datetime.datetime.fromtimestamp(data).strftime("%Y/%m/%d %H:%M:%S")
        return dt

    def file_write(self, data: str) -> None:
        """データをファイルに書き込む。

        指定されたデータをファイルに書き込みます。

        Args:
            data (str): 書き込むデータ。

        Returns:
            None

        Example:
            >>> use_bitbank_api = UseBitbankApi()
            >>> data_to_write = "{'pair': 'btc_jpy', 'side': 'buy'}"
            >>> use_bitbank_api.file_write(data_to_write)

        Notes:
            - データは指定されたファイルパス（"./response.txt"）に書き込まれます。
            - ファイルが既に存在する場合は、上書きされます。
            - 書き込むデータは文字列として渡される必要があります。

        """
        with open("./response.txt", "w") as f:
            f.write(data)


if __name__ == "__main__":  # pragma: no cover
    """スポットオーダーの処理を実行して結果をファイルに書き込む。

    スポットオーダーを実行し、APIのレスポンスを取得します。
    レスポンスが正常な場合は、注文日時をUnix時間から変換してファイルに書き込みます。
    レスポンスがエラーの場合は、エラーメッセージをファイルに書き込みます。

    Notes:
        - スポットオーダーの詳細な処理は `spot_order` メソッド内で行われます。
        - ファイルへの書き込みは `file_write` メソッドが担当します。
        - ファイルへの書き込み先は "./response.txt" です。

    Example:
        $ python input_spot_order.py 5000
        実行時の引数や設定に応じた処理が実行され、結果がファイルに書き込まれます。
        $ python input_spot_order.py
        コマンドライン引数を指定しない場合は500円換算値でスポットオーダーが実行されます。
    """
    use_bitbank_api = UseBitbankApi()
    try:
        response = use_bitbank_api.spot_order("buy", "btc_jpy")
    except Exception as e:
        use_bitbank_api.file_write(str(e))
    else:
        response["ordered_at"] = use_bitbank_api.conv_unixtime(
            int(response["ordered_at"])
        )
        response_json = json.dumps(response)
        use_bitbank_api.file_write(response_json)
