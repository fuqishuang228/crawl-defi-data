import csv
import pandas as pd
from environ.constants import BINANCE_WALLETS, ETH_WALLETS


def wallet_info(jiexi) -> pd.DataFrame:
    """
    Function to get wallet info
    """

    # create a csv file to store wallet info
    with open(BINANCE_WALLETS, mode="w", encoding="utf-8-sig", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(
            [
                "name",
                "balance",
                "network",
                "walletAddress",
                "priceUsd",
                "balanceUSD",
                "updateTime",
            ]
        )

    # get lengs of walletAddresses
    lengs = len(jiexi["props"]["pageProps"]["reserveData"]["exchangeWallets"])

    # iterate to get and store wallet info
    for i in range(lengs):
        walletAddress = jiexi["props"]["pageProps"]["reserveData"]["exchangeWallets"][
            i
        ]["walletAddress"]
        name = jiexi["props"]["pageProps"]["reserveData"]["exchangeWallets"][i]["name"]
        network = jiexi["props"]["pageProps"]["reserveData"]["exchangeWallets"][i][
            "network"
        ]
        balance = jiexi["props"]["pageProps"]["reserveData"]["exchangeWallets"][i][
            "balance"
        ]
        priceUsd = jiexi["props"]["pageProps"]["reserveData"]["exchangeWallets"][i][
            "priceUsd"
        ]
        updateTime = jiexi["props"]["pageProps"]["reserveData"]["exchangeWallets"][i][
            "updateTime"
        ]
        balanceUSD = jiexi["props"]["pageProps"]["reserveData"]["exchangeWallets"][i][
            "balanceUSD"
        ]

        print(walletAddress, name, network, balance, priceUsd, updateTime, balanceUSD)
        with open(BINANCE_WALLETS, mode="a", encoding="utf-8-sig", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(
                [
                    name,
                    balance,
                    network,
                    walletAddress,
                    priceUsd,
                    balanceUSD,
                    updateTime,
                ]
            )

    return pd.read_csv(BINANCE_WALLETS, encoding="utf-8-sig")


def wallet_info_on_eth(all_wallets) -> pd.DataFrame:
    """
    Function to get wallet info on eth
    """

    # filter wallets on eth
    eth_w = all_wallets.loc[all_wallets["network"] == "Ethereum"].reset_index(drop=True)

    # delete some columns
    eth_w = eth_w.drop(["balance", "priceUsd", "balanceUSD", "updateTime"], axis=1)

    # save
    eth_w.to_csv(ETH_WALLETS, encoding="utf-8-sig")
    return eth_w
