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
def faucet(Faucet,erc20,accounts):
    return Faucet.deploy(erc20.address, {'from': accounts[0]})

def test_faucet_init(faucet,erc20,accounts):
    assert faucet.amountAllowed() == 100
    assert faucet.tokenContract() == erc20.address

def test_requestTokens(faucet,erc20,accounts):
    tx = erc20.mint(501, {'from':accounts[0]})
    print(tx.events)
    assert erc20.balanceOf(accounts[0]) == 501
    tx = erc20.transfer(faucet.address,501)
    print(tx.events)
    assert erc20.balanceOf(faucet.address) == 501
    tx = faucet.requestTokens({'from':accounts[3]})
    print(tx.events)
    print(erc20.balanceOf(faucet.address))
    print(erc20.balanceOf(accounts[3].address))
