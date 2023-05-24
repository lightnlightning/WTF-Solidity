#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def insertionsort(InsertionSort, accounts):
    return InsertionSort.deploy( {'from': accounts[0]})

def test_ifElseTest(insertionsort,accounts):
    assert insertionsort.ifElseTest(0) == True
    assert insertionsort.ifElseTest(1) == False


def test_forLoopTest(insertionsort,accounts):
    assert insertionsort.forLoopTest() == 45

def test_whileTest(insertionsort,accounts):
    assert insertionsort.forLoopTest() == 45


def test_doWhileTest(insertionsort,accounts):
    assert insertionsort.forLoopTest() == 45


def test_ternaryTest(insertionsort,accounts):
    print(insertionsort.ternaryTest(55,88))


def test_insertionSortWrong(insertionsort,accounts):
    list_test = [3,4,5]
    print(insertionsort.insertionSortWrong(list_test))


def test_insertionSort(insertionsort,accounts):
    list_test = [3,4,5]
    print(insertionsort.insertionSort(list_test))
