#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def arraytypes(ArrayTypes, accounts):
    return ArrayTypes.deploy( {'from': accounts[0]})



def test_initArray(arraytypes):
    assert arraytypes.initArray() == (1,3,4)

def test_arrayPush(arraytypes):
    tx = arraytypes.arrayPush()
    assert tx.return_value == (1,2,3)
    

@pytest.fixture(scope="module")
def structtypes(StructTypes, accounts):
    return StructTypes.deploy( {'from': accounts[0]})

def test_initStudent1(structtypes):
    structtypes.initStudent1()
    assert structtypes.student() == (11, 100)

def test_initStudent2(structtypes):
    structtypes.initStudent2()
    assert structtypes.student() == (1, 80)


def test_initStudent3(structtypes):
    structtypes.initStudent3()
    assert structtypes.student() == (3, 90)


def test_initStudent4(structtypes):
    structtypes.initStudent4()
    assert structtypes.student() == (4, 60)
    


@pytest.fixture(scope="module")
def enumtypes(EnumTypes, accounts):
    return EnumTypes.deploy( {'from': accounts[0]})


def test_enumtypes(enumtypes):
    assert enumtypes.enumToUint() == 0









