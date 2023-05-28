#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def hash_contract(Hash,accounts):
    return Hash.deploy( {'from': accounts[0]})

    
def test_abiencode(hash_contract,accounts):
    print( hash_contract.hash(32,'sdggdsf',accounts[0].address) )
    print( hash_contract.weak(b"0xAA") )
    print( hash_contract.strong('sdggdsf','kfdhks') )
