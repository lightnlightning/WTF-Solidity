#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def mapping(Mapping, accounts):
    return Mapping.deploy({'from': accounts[0]})


def test_init(mapping,accounts):
    for i in range(10):
        assert mapping.idToAddress(i) == '0x0000000000000000000000000000000000000000'

def test_writeMap(mapping,accounts):
    mapping.writeMap(
        33,
        "0x66aB6D9362d4F35596279692F0251Db635165871",
        {'from': accounts[0]}
    )
    assert mapping.idToAddress(33) == "0x66aB6D9362d4F35596279692F0251Db635165871"

