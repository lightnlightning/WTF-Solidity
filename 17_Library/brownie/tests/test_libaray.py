#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def strings(Strings, accounts):
    return Strings.deploy( {'from': accounts[0]})

@pytest.fixture(scope="module")
def uselibrary(strings,UseLibrary, accounts):
    return UseLibrary.deploy( {'from': accounts[0]})

def test_getString1(uselibrary):
     assert uselibrary.getString1(25) == "\x19"

def test_getString2(uselibrary):
     assert uselibrary.getString1(25) == "\x19"
