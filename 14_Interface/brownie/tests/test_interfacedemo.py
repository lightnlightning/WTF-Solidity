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

def test_getFirstName(baseimpl1):
    assert baseimpl1.getFirstName() == "Amazing"


def test_getLastName(baseimpl1):
    assert baseimpl1.getLastName() == "Ang"


def test_value(baseimpl1):
    assert baseimpl1.a() == 13
