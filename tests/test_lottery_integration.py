import time
from brownie import network
import pytest
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    fund_with_link,
    get_account,
)
from scripts.deploy_lottery import deploy_lottery


def test_can_pick_winner():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    account = get_account()
    starting_tx = lottery.startLottery({"from": account})
    # starting_tx.wait(1)

    # Act
    # enter lottery with multiple accounts
    tx = lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    # tx.wait(1)
    tx = lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    # tx.wait(1)
    fund_with_link(lottery)
    end_tx = lottery.endLottery({"from": account})
    # end_tx.wait(1)
    time.sleep(60)
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0
