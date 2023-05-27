#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def othercontract(OtherContract,accounts):
    return OtherContract.deploy( {'from': accounts[0]})

def test_getBalance(othercontract,accounts):
    assert othercontract.getBalance() == 0

def test_setX(othercontract,accounts,history):
    othercontract.setX(3232,{'from':accounts[0],'value':33})
    print(history[-1].events)
    assert othercontract.balance() == 33
    assert othercontract.getX() == 3232

@pytest.fixture(scope="module")
def callcontract(CallContract,accounts):
    return CallContract.deploy( {'from': accounts[0]})

def test_callSetX(callcontract,accounts,othercontract,history):
    assert callcontract.callSetX(othercontract.address, 555, {'from': accounts[0]})
    assert othercontract.getX() == 555

def test_callGetX(callcontract,accounts,othercontract):
    assert callcontract.callGetX(othercontract.address) == 0

def test_callGetX2(callcontract,accounts,othercontract):
    assert callcontract.callGetX2(othercontract.address) == 0

def test_setXTransferETH(callcontract,accounts,othercontract):
    assert callcontract.setXTransferETH(othercontract.address,23,{'value':777})
    assert othercontract.balance() == 777
