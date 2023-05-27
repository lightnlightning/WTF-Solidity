#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def fallback(Fallback, accounts):
    return Fallback.deploy( {'from': accounts[0]})

def test_fallback(fallback,accounts,history):
    accounts[1].transfer(fallback.address,1111,data='0x14')
    print(history[-1].events)

def test_receive(fallback,accounts,history):
    accounts[1].transfer(fallback.address,1111)
    print(history[-1].events)
