#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

#  @pytest.fixture(scope="module")
#  def base1(Base1, accounts):
#      return Base1.deploy( {'from': accounts[0]})

@pytest.fixture(scope="module")
def identifier(Identifier, accounts):
    return Identifier.deploy( {'from': accounts[0]})

def test_getExactDividedBy2And3(identifier,accounts):
    assert identifier.getExactDividedBy2And3(6) ==(3,2)

