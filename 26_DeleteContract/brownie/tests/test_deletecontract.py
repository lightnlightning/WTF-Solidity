#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def deletecontract(DeleteContract,accounts):
    return DeleteContract.deploy( {'from': accounts[0],'value':1111})

def test_init(deletecontract,accounts):
    assert deletecontract.value() == 10
    assert deletecontract.balance() == 1111
    
def test_getBalance(deletecontract,accounts):
    assert deletecontract.getBalance() == 1111

def test_deleteContract(deletecontract,accounts):
    before_accounts = accounts[0].balance()
    print(before_accounts)
    contract_balance = deletecontract.balance()
    print(contract_balance)
    contract_balance = deletecontract.balance()
    assert deletecontract.deleteContract()
    assert accounts[0].balance() == before_accounts + contract_balance
