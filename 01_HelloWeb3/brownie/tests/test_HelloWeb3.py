#!/usr/bin/python3

import pytest


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def helloweb3(HelloWeb3, accounts):
    return HelloWeb3.deploy( {'from': accounts[0]})

def test_string(helloweb3,accounts):
    assert helloweb3._string() == "Hello Web3!"
