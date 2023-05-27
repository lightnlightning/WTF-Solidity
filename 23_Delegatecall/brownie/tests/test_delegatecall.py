#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def c(C,accounts):
    return C.deploy( {'from': accounts[0]})

def test_c_init(c,accounts):
    assert c.num() == 0
    assert c.sender() == "0x0000000000000000000000000000000000000000"

def test_c_setVars(c,accounts):
    c.setVars(69,{'from':accounts[0]})
    assert c.num() == 69
    assert c.sender() == accounts[0].address

@pytest.fixture(scope="module")
def b(B,accounts):
    return B.deploy( {'from': accounts[0]})

def test_b_init(b,accounts):
    assert b.num() == 0
    assert b.sender() == "0x0000000000000000000000000000000000000000"

def test_b_callSetVars(c,b,accounts):
    b.callSetVars(c.address,69,{'from':accounts[0]})
    assert b.num() == 0
    assert b.sender() == "0x0000000000000000000000000000000000000000"
    assert c.num() == 69
    assert c.sender() == b.address

def test_delegatecallSetVars(c,b,accounts):
    b.delegatecallSetVars(c.address,77,{'from':accounts[0]})
    assert c.num() == 0
    assert c.sender() == "0x0000000000000000000000000000000000000000"
    assert b.num() == 77
    assert b.sender() == accounts[0]
