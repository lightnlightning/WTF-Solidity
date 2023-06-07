#!/usr/bin/python3

import pytest, time
import sys
sys.path.append("..")
from scripts import my_pymerkle


# 利用Merkle树树验证白名单（生成Merkle树的网页：https://lab.miguelmota.com/merkletreejs/example/）
# 选上Keccak-256, hashLeaves和sortPairs选项
# 4个叶子地址：
 # [
 # "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4", 
 # "0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2",
 # "0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db",
 # "0x78731D3Ca6b7E34aC0F824c42a7cC18A495cabaB"
 # ]
# 第一个地址对应的merkle proof
 # [
 # "0x999bf57501565dbd2fdcea36efa2b9aef8340a8901e3459f4a4c926275d36cdb",
 # "0x4726e4102af77216b09ccd94f40daa10531c87c4d60bba7f3b3faf5ff9f19b3c"
 # ]
# Merkle root: 0xeeefd63003e0e702cb41cd0043015a6e26ddb38073cc6ffeb0ba3e808ba8c097


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

# root ='0xeeefd63003e0e702cb41cd0043015a6e26ddb38073cc6ffeb0ba3e808ba8c097'
# proof = [
    # "999bf57501565dbd2fdcea36efa2b9aef8340a8901e3459f4a4c926275d36cdb",
    # "4726e4102af77216b09ccd94f40daa10531c87c4d60bba7f3b3faf5ff9f19b3c"
# ]

list_data = [
    "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4", 
    "0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2",
    "0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db",
    "0x72731D3Ca6b7E34aC0F824c42a7cC18A495c31aB",
    "0x68C720746dD49B06a26eBaA11105A999940AcC46",
    "0x6b24EE1CE985A0A443e041378CB1C80b37d35829",
    "0x2352298C97034Ada7aD03b6996445e454fc4a147",
    "0x13AbCcE560f57f62dE48C9473dfc220377582397",
    "0x6a1ae5f0aab76b09d8B71aD820eFdA7ffd37cEfA",
    "0xdE1f12bCAf6De227cB5DAcEf50cD44dAF5AD0364",
    "0xE9fbdC9a6677B022f42c493bdc7204BF6481691f",
    "0xfAB043609bb20eA069d43E57B0A819303F0f65e8",
    "0x529e7dFA27075b9b67aB2f1285a582c3a655BE3A",
    "0x2A6cC7a08a60163cDF00CBc011A3dFE361DF5B80"
    ]
# list_data = ['a','b','c','d','e'] 
# tree_root = m.build_tree(list_data,sort_leaves=True,ishex=False)
root = None
proof = None
verify = list_data[3]

@pytest.fixture(scope="module")
def mk_py():
    m = my_pymerkle.MerkleTree('keccak')
    tree_root = m.build_tree(list_data,sort_leaves=False,ishex=True)
    proof_list = m.get_proof(tree_root,verify,ishex=True)
    global root, proof
    root = tree_root.Value
    proof = proof_list
    # return m, tree_root, proof_list

@pytest.fixture(scope="module")
def merkletree(mk_py,MerkleTree,accounts):
    return MerkleTree.deploy("WTF Dutch Auctoin","WTF Dutch Auctoin",root, {'from': accounts[0]})

def test_init(merkletree,accounts):
    assert merkletree.name() == "WTF Dutch Auctoin"
    assert merkletree.symbol() == "WTF Dutch Auctoin"
    assert merkletree.root() == '0x' + root
    # print(merkletree.root())
    # print(root)
    assert merkletree.mintedAddress(accounts[0]) == False

def test_mint(merkletree,accounts):
    assert merkletree.mintedAddress(accounts[0]) == False
    merkletree.mint(verify,0,proof,{'from':accounts[0]})
    assert merkletree.mintedAddress(verify) == True
    print(proof)

def mk_py1(ver):
    m = my_pymerkle.MerkleTree('keccak')
    tree_root = m.build_tree(list_data,sort_leaves=False,ishex=True)
    proof_list = m.get_proof(tree_root,ver,ishex=True)
    return tree_root.Value, proof_list
    
@pytest.mark.parametrize('li',list_data)
def test_mint_1(li,MerkleTree,accounts):
    root_, proof_ = mk_py1(li)
    merkletree = MerkleTree.deploy("WTF Dutch Auctoin","WTF Dutch Auctoin",root_, {'from': accounts[0]})
    assert merkletree.mintedAddress(accounts[0]) == False
    merkletree.mint(li,0,proof_,{'from':accounts[0]})
    assert merkletree.mintedAddress(li) == True
