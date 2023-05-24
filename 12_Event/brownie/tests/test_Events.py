#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def events(Events, accounts):
    return Events.deploy( {'from': accounts[0]})

def test_init(events,accounts):
    assert events._balances(accounts[0]) == 0


def test__transfer(events,accounts):
    tx = events._transfer(
            accounts[1],
            accounts[2],
            8888 
            )
    assert events._balances(accounts[1]) == 9991112
    assert events._balances(accounts[2]) == 8888
    print(tx.events[-1])

