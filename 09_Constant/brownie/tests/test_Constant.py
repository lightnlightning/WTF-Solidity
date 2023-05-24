#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def constant(Constant, accounts):
    return Constant.deploy( {'from': accounts[0]})

def test_init(constant,accounts):
    print(constant.IMMUTABLE_ADDRESS())
    print(constant.IMMUTABLE_BLOCK())
    print(constant.IMMUTABLE_TEST())
    #  assert constant.IMMUTABLE_ADDRESS() == ""
    assert constant.IMMUTABLE_BLOCK() == 1
    assert constant.IMMUTABLE_TEST() == 9
