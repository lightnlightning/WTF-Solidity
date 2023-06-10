#!/usr/bin/python3

import pytest, time
from scripts import wtf_sig

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def wtf_signature():
    private_key = "0x227dbb8586117d55284e26620bc76534dfbd2394be34cf4a09cb775d593b6f2b"
    address = "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"
    type_list = ['address', 'uint256']
    value_list = [address, 0] 
    sv = wtf_sig.sign_verify(private_key,[type_list,value_list])
    return sv

@pytest.fixture(scope="module")
def ecdsa(ECDSA,accounts):
    return ECDSA.deploy({'from': accounts[0]})

@pytest.fixture(scope="module")
def signatureNFT(ecdsa,SignatureNFT,accounts,wtf_signature):
    signer = wtf_signature.address
    return SignatureNFT.deploy("WTF Dutch Auctoin","WTF Dutch Auctoin", signer, {'from': accounts[0]})

def test_init(signatureNFT,accounts,wtf_signature):
    signer = wtf_signature.address
    assert signatureNFT.name() == "WTF Dutch Auctoin"
    assert signatureNFT.symbol() == "WTF Dutch Auctoin"
    assert signatureNFT.signer() == signer
    tx = signatureNFT.mint(
                wtf_signature.messages[1][0],
                wtf_signature.messages[1][1],
                wtf_signature.signature.signature
                )
    print(tx.events)
