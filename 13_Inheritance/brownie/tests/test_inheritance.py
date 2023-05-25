#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

#  @pytest.fixture(scope="module")
#  def yeye(Yeye, accounts):
#      return Yeye.deploy( {'from': accounts[0]})

#  def test_yeye_hip(yeye,accounts):
#      tx = yeye.hip()
#      print(tx.events[-1])

#  def test_yeye_pop(yeye,accounts):
#      tx = yeye.pop()
#      print(tx.events[-1])

#  def test_yeye_yeye(yeye,accounts):
#      tx = yeye.yeye()
#      print(tx.events[-1])


#  @pytest.fixture(scope="module")
#  def baba(Baba, accounts):
#      return Baba.deploy( {'from': accounts[0]})

#  def test_baba_hip(baba,accounts):
#      tx = baba.hip()
#      print(tx.events[-1])

#  def test_baba_pop(baba,accounts):
#      tx = baba.pop()
#      print(tx.events[-1])

#  def test_baba_baba(baba,accounts):
#      tx = baba.baba()
#      print(tx.events[-1])




@pytest.fixture(scope="module")
def erzi(Erzi, accounts):
    return Erzi.deploy( {'from': accounts[0]})

def test_erzi_hip(erzi,accounts):
    tx = erzi.hip()
    print(tx.events[-1])

def test_erzi_pop(erzi,accounts):
    tx = erzi.pop()
    print(tx.events[-1])

def test_erzi_callParent(erzi,accounts):
    tx = erzi.callParent()
    print(tx.events[-1])

def test_erzi_callParentSuper(erzi,accounts):
    tx = erzi.callParentSuper()
    print(tx.events[-1])
    
def test_erzi_parents(erzi,accounts):
    tx = erzi.baba()
    print(tx.events[-1])
    tx = erzi.yeye()
    print(tx.events[-1])


@pytest.fixture(scope="module")
def b(B, accounts):
    return B.deploy( {'from': accounts[0]})


def test_b(b,accounts):
    assert b.a() == 1


@pytest.fixture(scope="module")
def c(C, accounts):
    return C.deploy(10, {'from': accounts[0]})

def test_c(c,accounts):
    assert c.a() == 100
