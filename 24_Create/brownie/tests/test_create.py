#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def pair(Pair,accounts):
    return Pair.deploy( {'from': accounts[0]})

def test_pair_init(pair,accounts):
    assert pair.factory() == accounts[0].address
    assert pair.token0() == "0x0000000000000000000000000000000000000000"
    assert pair.token1() == "0x0000000000000000000000000000000000000000"
    
def test_initialize(pair,accounts):
    pair.initialize(
            accounts[1],
            accounts[2]
            )
    assert pair.factory() == accounts[0].address
    assert pair.token0() == accounts[1]
    assert pair.token1() == accounts[2]

@pytest.fixture(scope="module")
def pairfactory(PairFactory,accounts):
    return PairFactory.deploy( {'from': accounts[0]})

def test_PaerFactory_init(pairfactory,accounts):
    assert pairfactory.getPair(
            "0x0000000000000000000000000000000000000000",
            "0x0000000000000000000000000000000000000000"
            ) == "0x0000000000000000000000000000000000000000"
    #  assert pairfactory.allPairs() == [] 
    
def test_createPair(pair,pairfactory,accounts,Pair,Contract):
    tx = pairfactory.createPair(accounts[1],accounts[2])
    pp = Contract.from_abi("Pair", tx.return_value, Pair.abi)
    assert pp.factory() == pairfactory.address
    assert pp.token0() == accounts[1]
    assert pp.token1() == accounts[2]

    assert pairfactory.getPair(
            accounts[1],
            accounts[2],
            ) == tx.return_value
    assert pairfactory.allPairs(0) ==  tx.return_value
