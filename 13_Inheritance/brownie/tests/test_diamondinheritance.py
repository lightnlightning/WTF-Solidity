#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def god(God, accounts):
    return God.deploy( {'from': accounts[0]})

def test_foo1(god,accounts):
    tx = god.foo()
    print(tx.events[-1]) 

def test_bar1(god,accounts):
    print(god.foo().events[-1]) 


@pytest.fixture(scope="module")
def adam(Adam, accounts):
    return Adam.deploy( {'from': accounts[0]})

def test_foo2(adam,accounts):
    print(adam.foo().events[-1]) 

def test_bar2(adam,accounts):
    print(adam.bar().events) 


@pytest.fixture(scope="module")
def eve(Eve, accounts):
    return Eve.deploy( {'from': accounts[0]})

def test_foo3(eve,accounts):
    print(eve.foo().events) 

def test_bar3(eve,accounts):
    print(eve.bar().events) 




@pytest.fixture(scope="module")
def pp(people, accounts):
    return people.deploy( {'from': accounts[0]})

def test_foo4(pp,accounts):
    print(pp.foo().events) 


def test_bar4(pp,accounts):
    print(pp.foo().events) 
