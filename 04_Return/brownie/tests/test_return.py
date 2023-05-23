#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def d_return(Return, accounts):
    return Return.deploy( {'from': accounts[0]})

def test_returnMultiple(d_return):
    a=d_return.returnMultiple()
    print(d_return.returnMultiple())

def test_returnNamed(d_return):
    a = d_return.returnNamed()
    print(a)


def test_returnNamed2(d_return):
    a = d_return.returnNamed2()
    print(a)
    


def test_readReturn(d_return):
    a = d_return.readReturn()
    print(a)
