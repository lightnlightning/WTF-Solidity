#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def erc20(ERC20,accounts):
    return ERC20.deploy('bbd', 'bbd', {'from': accounts[0]})

#  def test_init(erc20,accounts):
#      assert erc20.balanceOf(accounts[0].address) == 0
#      assert erc20.allowance(accounts[0].address,accounts[1]) == 0
#      assert erc20.totalSupply() == 0
#      assert erc20.name() == 'bbd'
#      assert erc20.symbol() == 'bbd'
#      assert erc20.decimals() == 18

#  def test_mint(erc20,accounts):
#      tx = erc20.mint(1, {'from':accounts[0]})
#      print(tx.events)
#      assert erc20.balanceOf(accounts[0]) == 1

#  def test_transfer(erc20,accounts):
#      erc20.mint(500, {'from':accounts[0]})
#      tx = erc20.transfer(accounts[1].address, 500, {'from':accounts[0]})
#      print(tx.events)
#      assert erc20.balanceOf(accounts[1]) == 500

#  def test_approve(erc20,accounts):
#      erc20.mint(500, {'from':accounts[0]})
#      tx = erc20.approve(accounts[1].address, 500, {'from':accounts[0]})
#      print(tx.events)
#      assert erc20.allowance(accounts[0],accounts[1]) == 500

#  def test_transferFrom(erc20,accounts):
#      erc20.mint(500, {'from':accounts[0]})
#      tx = erc20.approve(accounts[1].address, 500, {'from':accounts[0]})
#      print(tx.events)
#      assert erc20.allowance(accounts[0],accounts[1]) == 500
#      tx = erc20.transferFrom(accounts[0],accounts[3],500,{'from':accounts[1]})
#      print(tx.events)
#      assert erc20.balanceOf(accounts[3]) == 500

#  def test_burn(erc20,accounts):
#      tx = erc20.mint(1111, {'from':accounts[0]})
#      print(tx.events)
#      assert erc20.balanceOf(accounts[0]) == 1111
#      tx = erc20.burn(1111)
#      print(tx.events)
#      assert erc20.balanceOf(accounts[0]) == 0

@pytest.fixture(scope="module")
def airdrop(Airdrop,erc20,accounts):
    return Airdrop.deploy({'from': accounts[0]})

def test_multiTransferToken(airdrop,accounts,erc20):
    list_addresses = [accounts[2],accounts[3]]
    list_amounts = [100,300]
    tx = erc20.mint(500, {'from':accounts[0]})
    print(tx.events)
    tx = erc20.approve(airdrop.address, 500, {'from':accounts[0]})
    print(tx.events)
    assert erc20.allowance(accounts[0],airdrop.address) == 500
    tx = airdrop.multiTransferToken(
            erc20.address,
            list_addresses,
            list_amounts,
            )
    print(tx.events)
    assert erc20.balanceOf(accounts[2]) == 100
    assert erc20.balanceOf(accounts[3]) == 300
    

def test_multiTransferETH(airdrop,accounts,erc20):
    list_addresses = [accounts[2],accounts[3]]
    list_amounts = [100,300]
    tx = airdrop.multiTransferETH(
            list_addresses,
            list_amounts,
            {'value':400} 
            )
    print(accounts[0].balance())
    print(accounts[2].balance())
    print(accounts[3].balance())
