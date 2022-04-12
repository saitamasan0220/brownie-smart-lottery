from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account, fund_with_link
from brownie import Lottery, accounts, config, network, exceptions
from scripts.deploy_lottery import deploy_lottery
from web3 import Web3
import pytest

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

def test_cant_enter_unless_started():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    # Act/Assert
    with pytest.raises(exceptions.VirtualMachineError):
        lottery.enter({"from": get_account(), "value": lottery.getEntranceFee()})

def test_can_start_and_enter_lottery():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    account = get_account()
    starting_tx = lottery.startLottery({"from": account})
    starting_tx.wait(1)
    # Act
    tx = lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    tx.wait(1)
    # Assert
    assert lottery.players(0) == account

def test_can_end_lottery():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    account = get_account()
    starting_tx = lottery.startLottery({"from": account})
    starting_tx.wait(1)
    # Act
    tx = lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    tx.wait(1)

    fund_with_link(lottery)
    end_tx = lottery.endLottery({"from": account})
    end_tx.wait(1)
    assert lottery.lottery_state() == 2


