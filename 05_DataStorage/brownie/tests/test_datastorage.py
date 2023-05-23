#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def datastorage(DataStorage, accounts):
    return DataStorage.deploy( {'from': accounts[0]})

def test_init(datastorage):
    x = [1,2,3]
    for i in range(3):
        assert x[i] == datastorage.x(i) 


def test_fStorage(datastorage):
    datastorage.fStorage() 
    assert datastorage.x(0) == 100



def test_fMemory(datastorage):
    datastorage.fMemory() 
    assert datastorage.x(0) == 1
    assert datastorage.x(1) == 2


@pytest.fixture(scope="module")
def variables(Variables, accounts):
    return Variables.deploy( {'from': accounts[0]})


def test_init(variables):
    assert variables.x() == 1
    assert variables.y() == 0
    assert variables.z() == ""

def test_foo(variables):
    variables.foo() 
    assert variables.x() == 5
    assert variables.y() == 2

    #  z = "0xAA";  //这个字符brownie 有报错，brownie 有bug,remix验证可以通过
    assert variables.z() == "some string"


def test_bar(variables):
    assert variables.bar() == 4


def test_global1(variables):
    #  print(variables.global())
    #  locals global
    #  variables.global()   global函数与python的global重名,换成global1
    print(variables.global1())

def test_weiUnit(variables):
    assert variables.weiUnit() == 1

def test_gweiUnit(variables):
    assert variables.gweiUnit() == 1e9

def test_etherUnit(variables):
    assert variables.etherUnit() == 1e18

def test_secondsUnit(variables):
    assert variables.secondsUnit() == 1

def test_minutesUnit(variables):
    assert variables.minutesUnit() == 60

def test_hoursUnit(variables):
    assert variables.hoursUnit() == 3600

def test_daysUnit(variables):
    assert variables.daysUnit() == 86400


def test_weeksUnit(variables):
    assert variables.weeksUnit() == 604800

