#!/usr/bin/python3
from web3 import Web3
from eth_account.messages import encode_defunct
from eth_account import Account

class sign_verify:
    def __init__(self,private_key,messages):
        self.private_key = private_key
        self.address = Account.from_key(private_key).address
        self.messages = messages
        self.signature = None
        self.verify = None
        self.init()

    def init(self):
        self.signature = self.sig_message(self.messages[0], self.messages[1], self.private_key)
        self.verify = self.verify_message(self.messages[0], self.messages[1], self.signature.signature)

    def sig_message(self, type_list:list=[], value_list:list=[], pri_key:hex='')->object:
        #打包信息 solidity 合约的格式 hash计算
        msg = Web3.solidityKeccak(type_list, value_list)
        #构造以太坊格式签名信息
        #  msg + b'thereum Signed Message:\n32'
        message = encode_defunct(hexstr=msg.hex())
        #签名
        return Account.sign_message(message, private_key=pri_key)

    def verify_message(self, type_list:list=[], value_list:list=[], signature:bytes=None)->hex:
        #打包信息 solidity 合约的格式 hash计算
        msg = Web3.solidityKeccak(type_list, value_list)
        #构造可签名信息
        #  msg + b'thereum Signed Message:\n32'
        message = encode_defunct(hexstr=msg.hex())
        #恢复出签名的地址
        return Account.recover_message(signable_message=message, signature=signature)

# if __name__ == '__main__':
def main():
    private_key = "0x227dbb8586117d55284e26620bc76534dfbd2394be34cf4a09cb775d593b6f2b"
    address = "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"
    type_list = ['address', 'uint256']
    value_list = [address, 0] 
    sv = sign_verify(private_key,[type_list,value_list])
    print(sv.private_key)
    print(sv.address)
    print(sv.messages)
    print(sv.signature)
    print(sv.signature.signature.hex())
    print(len(sv.signature.signature))
    # 分割signature
    print(sv.signature.signature[:31].hex())
    print(sv.signature.signature[32:63].hex())
    print(sv.signature.signature[64:65].hex())
    pass
    print(hex(sv.signature['r']))
    print(hex(sv.signature['s']))
    print(hex(sv.signature['v']))
    print(sv.verify)
