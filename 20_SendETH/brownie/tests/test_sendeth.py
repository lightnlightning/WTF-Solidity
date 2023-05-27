#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def sendETH(SendETH, accounts,history):
    ss=SendETH.deploy( {'from': accounts[0],'value':4432})
    return ss

def test_sendETH_init(sendETH,accounts):
    assert sendETH.balance() == 4432

def test_transferETH(sendETH,accounts):
    before_account = accounts[3].balance()
    before_send = sendETH.balance() 
    sendETH.transferETH(accounts[3],444)
    assert accounts[3].balance() == before_account + 444
    assert sendETH.balance() == before_send - 444

def test_callETH(sendETH,accounts):
    before_account = accounts[3].balance()
    before_send = sendETH.balance() 
    sendETH.callETH(accounts[3],444)
    assert accounts[3].balance() == before_account + 444
    assert sendETH.balance() == before_send - 444

@pytest.fixture(scope="module")
def receiveETH(ReceiveETH, accounts):
    return ReceiveETH.deploy( {'from': accounts[0]} )

def test_receiveETH(receiveETH,accounts,history):
    before_account = accounts[3].balance()
    before_rece = receiveETH.balance() 
    accounts[3].transfer(receiveETH.address,888)
    print(history[-1].events)
    assert accounts[3].balance() == before_account - 888
    assert receiveETH.balance() == before_rece + 888
    assert receiveETH.getBalance() == before_rece + 888
