import eth_account
from web3 import Web3
from eth_account.messages import encode_structured_data
from eth_account import Account

class sign_verify:
    def __init__(self,private_key,domain,value):
        self.private_key = private_key
        self.address = Account.from_key(private_key).address
        self.messages = {
            "types": {
                "EIP712Domain": [
                    {"name": "name", "type": "string"},
                    {"name": "version", "type": "string"},
                    {"name": "chainId", "type": "uint256"},
                    {"name": "verifyingContract", "type": "address"}
                ],
                "Storage": [
                    {"name": 'spender', "type": 'address'},
                    {"name": 'number', "type": 'uint256'}
                ]
            },
            "domain": domain,
            "primaryType": 'Storage',
            "message": value
        }
        self.signature = None
        self.verify = None
        self.init()

    def init(self):
        self.signature = self.sig_message(self.messages, self.private_key)
        self.verify = self.verify_message(self.messages, self.signature.signature)

    def sig_message(self, msg:dict={}, pri_key:hex='')->object:
        # 需要先对结构数据进行编码
        encoded_data = encode_structured_data(msg)
        # 再进行签名
        # signed_message = web3.eth.account.sign_message(encoded_data, private_key)
        return Account.sign_message(encoded_data, private_key=pri_key)

    def verify_message(self, msg:dict={}, signature:bytes=None)->hex:
        # 需要先对结构数据进行编码
        encoded_data = encode_structured_data(msg)
        #恢复出签名的地址
        return Account.recover_message(encoded_data, signature=signature)

def main():
# if __name__ == '__main__':
    web3 = Web3()
    private_key = '0xbbfbee4961061d506ffbb11dfea64eba16355cbf1d9c29613126ba7fec0aed5d'
    domain = {
        "name": "EIP712Storage",
        "version": "1",
        "chainId": web3.eth.chain_id,
        "verifyingContract": "0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87",
    }
    value = {
        "spender": '0x66aB6D9362d4F35596279692F0251Db635165871',
        "number": 0,
    }

    sv = sign_verify(private_key,domain, value)
    print(sv.signature['signature'].hex())
    print(hex(sv.signature['r']))
    print(hex(sv.signature['s']))
    print(hex(sv.signature['v']))
    print(sv.address)
    print(sv.verify)
    print(sv.messages)
