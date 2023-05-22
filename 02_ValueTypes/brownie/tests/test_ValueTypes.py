#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def valuetypes(ValueTypes, accounts):
    return ValueTypes.deploy( {'from': accounts[0]})

def test_values(valuetypes,accounts):
    #  assert valuetypes._string() == "Hello Web3!"
    assert valuetypes._bool() == True 
    assert valuetypes._bool1() == False
    assert valuetypes._bool2() == False
    assert valuetypes._bool3() == True
    assert valuetypes._bool4() == False
    assert valuetypes._bool5() == True

    assert valuetypes._int() == -1
    assert valuetypes._uint() == 1
    assert valuetypes._number() == 20220330
    assert valuetypes._number1() == 20220331
    assert valuetypes._number2() == 4
    assert valuetypes._number3() == 1
    assert valuetypes._numberbool() == True

    assert valuetypes._address() == "0x33A4622B82D4c04a53e170c638B944ce27cffce3"
    #  无法调用_address1的成员变量balance,只能在合约内使用
    assert valuetypes._address1() == "0x33A4622B82D4c04a53e170c638B944ce27cffce3"
    assert accounts[1].address == "0x33A4622B82D4c04a53e170c638B944ce27cffce3"
    assert valuetypes.balance() == accounts[1].balance()
    
    print(valuetypes._byte32())
    print(valuetypes._byte())
    print(valuetypes.enumToUint())
