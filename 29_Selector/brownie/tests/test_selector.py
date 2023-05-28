#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def selector(Selector,accounts):
    return Selector.deploy( {'from': accounts[0]})

    
def test_mint(selector,accounts):
    tx = selector.mint(accounts[1].address)
    print(tx.events)

def test_mintselector(selector,accounts):
    print(selector.mintSelector())

def test_callwithsignature(selector,accounts):
    tx = selector.callWithSignature()
    print(tx.return_value)
    print(tx.events)
