#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def functiontypes(FunctionTypes, accounts):
    return FunctionTypes.deploy( {'from': accounts[0],'value':89})

def test_minusCall(functiontypes):
    for id in range(1,5):
        functiontypes.minusCall()    # 只能减到5,不然会数据溢出
        assert functiontypes.number() == 5 - id
    
