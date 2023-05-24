#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def initialvalue(InitialValue, accounts):
    return InitialValue.deploy({'from': accounts[0]})


def test_init(initialvalue,accounts):
    pass

def test_d(initialvalue,accounts):
    assert initialvalue._bool2() == True
    initialvalue.d()
    assert initialvalue._bool2() == False
