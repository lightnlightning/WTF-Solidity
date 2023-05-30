#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def wtfape(WTFApe,accounts):
    return WTFApe.deploy('bbd', 'bbd', {'from': accounts[0]})

def test_init(wtfape,accounts):
    assert wtfape.balanceOf(accounts[0]) == 0
    assert wtfape.isApprovedForAll(accounts[0],accounts[1]) == False
    assert wtfape.name() == 'bbd'
    assert wtfape.symbol() == 'bbd'

def test_mint(wtfape,accounts):
    tx = wtfape.mint(accounts[1],0)
    print(tx.events)
    assert wtfape.balanceOf(accounts[1]) == 1
    assert wtfape.ownerOf(0) == accounts[1]

def test_transfer(wtfape,accounts):
    wtfape.mint(accounts[0],2)
    tx = wtfape.transferFrom(accounts[0], accounts[1], 2, {'from':accounts[0]})
    print(tx.events)
    assert wtfape.balanceOf(accounts[1]) == 1
    assert wtfape.ownerOf(2) == accounts[1]

def test_safeTransferFrom(wtfape,accounts):
    wtfape.mint(accounts[0],2)
    tx = wtfape.safeTransferFrom(accounts[0], accounts[1], 2, {'from':accounts[0]})
    print(tx.events)
    assert wtfape.balanceOf(accounts[1]) == 1
    assert wtfape.ownerOf(2) == accounts[1]

def test_approve(wtfape,accounts):
    wtfape.mint(accounts[0],2)
    tx = wtfape.approve(accounts[2], 2)
    print(tx.events)
    assert wtfape.getApproved(2) == accounts[2]


def test_setApprovalForAll(wtfape,accounts):
    wtfape.mint(accounts[0],0)
    wtfape.mint(accounts[0],1)
    tx = wtfape.setApprovalForAll(accounts[2], True)
    print(tx.events)
    assert wtfape.isApprovedForAll(accounts[0],accounts[2]) == True




def test_supportsInterface(wtfape,accounts,interface):
    dict_ierc165 = interface.IERC165.selectors
    bytes4 = int('0x00000000',16)
    for key in dict_ierc165.keys():
        bytes4 = bytes4 ^ int(key,16)
    return_bool = wtfape.supportsInterface(hex(bytes4))
    assert return_bool == True

    dict_ierc = interface.IERC721.selectors
    bytes4 = int('0x00000000',16)
    for key in dict_ierc.keys():
        if '0x01ffc9a7' == key :   # 721接口多继承了165接口的一个函数，剔除掉
            continue
        bytes4 = bytes4 ^ int(key,16)
    return_bool = wtfape.supportsInterface(hex(bytes4))
    assert return_bool == True

    dict_ierc = interface.IERC721Metadata.selectors
    bytes4 = int('0x00000000',16)
    for key in dict_ierc.keys():
        bytes4 = bytes4 ^ int(key,16)
    return_bool = wtfape.supportsInterface(hex(bytes4))
    assert return_bool == True

def test_tokenURI(wtfape,accounts):
    tx = wtfape.mint(accounts[1],0)
    print(tx.events)
    rv = wtfape.tokenURI(0)
    print(rv)
