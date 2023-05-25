#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def baseimpl1(BaseImpl1, accounts):
    return BaseImpl1.deploy( {'from': accounts[0]})

@pytest.fixture(scope="module")
def my_inter(my_interface,baseimpl1, accounts):
    return my_interface.deploy(baseimpl1.address, {'from': accounts[0]})

def test_getFN(my_inter):
    assert my_inter.getFN() == "Amazing"

def test_getLN(my_inter):
    assert my_inter.getLN() == "Ang"

