from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
# This is 2,000
INITIAL_VALUE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mock():
    print(f"The active network is: {network.show_active()}")
    print("Deploying mock...")
    if len(MockV3Aggregator) <= 0 :
        MockV3Aggregator.deploy(DECIMALS, INITIAL_VALUE, {"from": get_account()})
    print("Mock deployed")


def get_price_feed_address():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mock()
        return MockV3Aggregator[-1].address
