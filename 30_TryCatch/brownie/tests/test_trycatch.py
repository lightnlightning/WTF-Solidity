#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def onlyeven(OnlyEven,accounts):
    return OnlyEven.deploy(2, {'from': accounts[0]})

def test_onlyEven(onlyeven,accounts):
    return_value = onlyeven.onlyEven(22)
    print(return_value)

@pytest.fixture(scope="module")
def trycatch(TryCatch,accounts):
    return TryCatch.deploy({'from': accounts[0]})

def test_execute(trycatch,accounts):
    tx = trycatch.execute(22)
    print(tx.return_value)
    print(tx.events)

    tx = trycatch.execute(21)
    print(tx.return_value)
    print(tx.events)

def test_executeNew(trycatch,accounts):
    tx = trycatch.executeNew(22)
    print(tx.return_value)
    print(tx.events)

    tx = trycatch.executeNew(0)
    print(tx.return_value)
    print(tx.events)

    tx = trycatch.executeNew(1)
    print(tx.return_value)
    print(tx.events)

