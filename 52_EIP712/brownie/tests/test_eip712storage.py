#!/usr/bin/python3
import pytest, time
from web3 import Web3
from scripts import eip712storage

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def eip712_storage_sig(accounts,eip712_storage):
    private_key = '0xbbfbee4961061d506ffbb11dfea64eba16355cbf1d9c29613126ba7fec0aed5d' #accounts[0]的私钥
    domain = {
        "name": "EIP712Storage",
        "version": "1",
        "chainId": 1,
        "verifyingContract": eip712_storage.address
    }
    value = {
        "spender": accounts[0].address,
        "number": 89 
    }
    sv = eip712storage.sign_verify(private_key,domain, value)
    return sv

@pytest.fixture(scope="module")
def eip712_storage(EIP712Storage,accounts):
    return EIP712Storage.deploy( {'from': accounts[0]})

def test_init(eip712_storage,accounts):
    assert eip712_storage.retrieve() == 0

def test_permitstore(eip712_storage, eip712_storage_sig, accounts):
    signature = eip712_storage_sig.signature['signature']
    assert eip712_storage.retrieve() == 0
    tx = eip712_storage.permitStore(89,signature)
    assert eip712_storage.retrieve() == 89
