#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def errors(Errors, accounts):
    return Errors.deploy( {'from': accounts[0]})

def test_transferOwner1(errors,accounts):
    tx1 = errors.transferOwner1(0,accounts[0])

def test_transferOwner2(errors,accounts):
    tx2 = errors.transferOwner2(0,accounts[0])

def test_transferOwner3(errors,accounts):
    tx3 = errors.transferOwner3(0,accounts[0])


#  brownie test --disable-warnings -v -s -i
#  tx.gas_used
