"""
Crawl all wallet addresses of binance
"""

import re
import json
import requests
from environ.constants import PRO,URL,HEADERS
from environ.process.get_wallet_info import wallet_info,wallet_info_on_eth


if __name__ == "__main__":
    # Sends a GET request. Returns Response object
    req = requests.get(URL, headers=HEADERS, proxies=PRO)

    # get data of req
    html = req.text

    # get html json part of wallet
    htmljs = re.findall('type="application/json">(.*?)</script>', html)[0] #.是代表一个字符 *是多个 ？一个或者两个

    # parse
    jiexi = json.loads(htmljs)

    # get all wallet addresses of binance
    binance_wallets=wallet_info(jiexi)

    # get wallet on ETH
    eth_wallets=wallet_info_on_eth(binance_wallets)
