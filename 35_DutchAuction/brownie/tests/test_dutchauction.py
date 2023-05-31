#!/usr/bin/python3

import pytest, time

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass
# 打开终端设置出块时间为1秒，默认是不出块的。
# ganache-cli -b 1

@pytest.fixture(scope="module")
def dutchauction(DutchAuction,accounts):
    return DutchAuction.deploy( {'from': accounts[0]})

def test_init(dutchauction,accounts):
    assert dutchauction.balanceOf(accounts[0]) == 0
    assert dutchauction.isApprovedForAll(accounts[0],accounts[1]) == False
    assert dutchauction.name() == "WTF Dutch Auctoin"
    assert dutchauction.symbol() == "WTF Dutch Auctoin"
    assert dutchauction.COLLECTOIN_SIZE() == 10000
    assert dutchauction.AUCTION_START_PRICE() == 1e+18
    assert dutchauction.AUCTION_END_PRICE() == 1e+17
    assert dutchauction.AUCTION_TIME() == 10
    assert dutchauction.AUCTION_DROP_INTERVAL() == 1
    assert dutchauction.AUCTION_DROP_PER_STEP() == 9e+16
    dutchauction.auctionMint(1,{'from': accounts[0],'value':10*(1e+18)})
    assert dutchauction.totalSupply() == 1
    timeArray = time.localtime(dutchauction.auctionStartTime())
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)

# 一个函数一个测试，一起测试块时间已经到拍卖结束时间了

#  def test_getAuctionPrice(dutchauction,accounts,chain):
#      for s in range(15):
#          price = dutchauction.getAuctionPrice()
#          print(price)
#          time.sleep(1)

#  def test_auctionMint(dutchauction,accounts):
#      for i in range(13):
#          cost = accounts[0].balance()
#          tx = dutchauction.auctionMint(1,{'from': accounts[0],'value':10*(1e+18)})
#          tx.wait(1)          # 等待出一个块之后在接着抢购
#          cost = cost - accounts[0].balance()
#          print(cost)         # 每次抢购花费多少
#      print(dutchauction.balance())


def test_withdrawMoney(dutchauction,accounts):
    dutchauction.auctionMint(1,{'from': accounts[0],'value':10*(1e+18)})
    print(dutchauction.balance())
    print(accounts[0].balance())
    dutchauction.withdrawMoney()
    print(dutchauction.balance())
    print(accounts[0].balance())

