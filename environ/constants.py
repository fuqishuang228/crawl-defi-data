"""
Constants for the project
"""

from environ.settings import PROJECT_ROOT

BINANCE_WALLETS=f"{PROJECT_ROOT}/data/binance_wallet.csv"
ETH_WALLETS=f"{PROJECT_ROOT}/data/binance_eth_wallet.csv"

PRO= {"https": "127.0.0.1:11223", "http": "127.0.0.1:11223"}

URL = "https://coinmarketcap.com/exchanges/binance/"

HEADERS= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}