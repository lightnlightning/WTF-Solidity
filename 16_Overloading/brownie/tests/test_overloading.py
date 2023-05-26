#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def overload(Overload, accounts):
    return Overload.deploy( {'from': accounts[0]})

def test_saySomething(overload,accounts):
     assert overload.saySomething("你好") == "你好"

def test_f(overload,accounts):
     assert overload.f(22,22) == 22

def test_f1(overload,accounts):
     assert overload.f(2) == 2
