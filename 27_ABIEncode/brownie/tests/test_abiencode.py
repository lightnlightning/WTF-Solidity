#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def abiencode(ABIEncode,accounts):
    return ABIEncode.deploy( {'from': accounts[0]})

    
def test_abiencode(abiencode,accounts):
    abiencode_return = abiencode.encode()
    print(abiencode.encode())
    print("--------------------------------")
    print(abiencode.encodePacked())
    print("--------------------------------")
    print(abiencode.encodeWithSignature())
    print("--------------------------------")
    print(abiencode.encodeWithSelector())
    print("--------------------------------")
    print(abiencode.decode(abiencode_return))
    print(abiencode.decode(abiencode.encode()))

