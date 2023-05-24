#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def owner(Owner, accounts):
    return Owner.deploy( {'from': accounts[0]})

def test_init(owner,accounts):
    assert owner.owner() == "0x66aB6D9362d4F35596279692F0251Db635165871"


def test_changeOwner(owner,accounts):
    assert owner.changeOwner(accounts[1])
    owner.owner() == accounts[1]


def test_test(owner,accounts):
    tx = owner.test()
    assert tx.return_value == 1
