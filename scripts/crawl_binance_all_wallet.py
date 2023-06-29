"""
Crawl all wallet addresses of binance
"""
import json
import re

import requests

from environ.constants import HEADERS, PRO, URL
from environ.process.get_wallet_info import wallet_info, wallet_info_on_eth

if __name__ == "__main__":
    # Sends a GET request. Returns Response object
    req_url = requests.get(URL, headers=HEADERS, proxies=PRO)

    # get data of req
    html_url = req_url.text

    # get html json part of wallet
    html_json = re.findall('script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html_url)[0] #.是代表一个字符 *是多个 ？一个或者两个

    # parse
    jiexi_json_data = json.loads(html_json)

    # get all wallet addresses of binance
    binance_wallets=wallet_info(jiexi_json_data)

    # get wallet on ETH
    eth_wallets=wallet_info_on_eth(binance_wallets)

    