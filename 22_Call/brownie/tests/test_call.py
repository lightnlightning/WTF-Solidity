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
def call(Call,accounts):
    return Call.deploy( {'from': accounts[0]})

def test_callSetX(call,accounts,othercontract,history):
    call.callSetX(othercontract.address, 555, {'from': accounts[0]})
    print(history[-1].events)
    assert othercontract.getX() == 555

def test_callGetX(history,call,accounts,othercontract):
    call.callGetX(othercontract.address)
    assert history[-1].return_value == 0
    print(history[-1].events)

def test_callNonExist(history,call,accounts,othercontract):
    assert call.callNonExist(othercontract.address)
    print(history[-1].events)

