#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def interactbayc(interactBAYC, accounts):
    return interactBAYC.deploy( {'from': accounts[0]})

def test_interactbayc(interactbayc,accounts):
    #  assert interactbayc.balanceOfBAYC() == "Amazing"
    pass


