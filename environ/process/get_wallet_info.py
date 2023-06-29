"""
Function to get wallet info
"""
import pandas as pd

from environ.constants import BINANCE_WALLETS, ETH_WALLETS


def wallet_info(jiexi_json_data: dict) -> pd.DataFrame:
    """
    Function to get wallet info
    """

    # create a dict to store wallet info
    wallet_data_dict = {
        "wallet_name": [],
        "wallet_balance": [],
        "network": [],
        "wallet_address": [],
        "price_usd": [],
        "balance_usd": [],
        "update_time": [],
    }

    # create a dict to store wallet column and json key
    wallet_data_jiexi_json_dict = {
        "wallet_name": "name",
        "wallet_balance": "balance",
        "network": "network",
        "wallet_address": "walletAddress",
        "price_usd": "priceUsd",
        "balance_usd": "balanceUSD",
        "update_time": "updateTime",
    }

    # get lengs of walletAddresses
    wallet_num = len(
        jiexi_json_data["props"]["pageProps"]["reserveData"]["exchangeWallets"]
    )

    # iterate to get and store wallet info
    for _ in range(wallet_num):
        # get target wallet json info
        target_wallet_json = jiexi_json_data["props"]["pageProps"]["reserveData"][
            "exchangeWallets"
        ][_]

        # iterate to get and store wallet info
        for name, value in wallet_data_jiexi_json_dict.items():
            # store wallet info
            wallet_data_dict[name].append(target_wallet_json[value])

    # change date_dict to dataframe
    wallet_data_df = pd.DataFrame(wallet_data_dict)

    # save data_dict to csv
    wallet_data_df.to_csv(BINANCE_WALLETS, encoding="utf-8-sig")

    return wallet_data_df


def wallet_info_on_eth(all_wallets: pd.DataFrame) -> pd.DataFrame:
    """
    Function to get wallet info on eth
    """

    # filter wallets on eth
    eth_wallet_df = all_wallets.loc[all_wallets["network"] == "Ethereum"].reset_index(
        drop=True
    )

    # delete some columns
    eth_wallet_df = eth_wallet_df.drop(
        ["wallet_balance", "price_usd", "update_time"], axis=1
    )

    # save eth_wallet_df to csv
    eth_wallet_df.to_csv(ETH_WALLETS, encoding="utf-8-sig")

    return eth_wallet_df
