from brownie import Lottery, accounts, config, network
from web3 import Web3
from scripts.deploy_lottery import deploy_lottery
import pytest
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS
from dotenv import load_dotenv

load_dotenv()


def test_get_entrance_fee():
    #  account = accounts[0]
    #  lottery = Lottery.deploy(config["networks"][network.show_active()]["eth_usd_price_feed"], {"from": account},)
    #  assert lottery.getEntranceFee() > lottery.getWeiPriceFromDollar(35)
    #  assert lottery.getEntranceFee() < lottery.getWeiPriceFromDollar(55)
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    expected_entrance_fee = lottery.getWeiPriceFromDollar(50)
    entrance_fee = lottery.getEntranceFee()
    assert expected_entrance_fee == entrance_fee
