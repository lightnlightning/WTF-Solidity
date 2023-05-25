#!/usr/bin/python3
from brownie import accounts, config, network
import csv 

# 自己定义的账户

def readCSV(row = 0, col = 2, path='./scripts/wallets.csv' ):
    #  row ['id','address','privateKey','publicKey',...]
    privateKey = 0
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(csv_file, None)
        for user in reader:
            if(user[0] == str(row)):
               privateKey = user[col]
               break
    return privateKey

def readCSV_list(row_f = 0, row_l = 0, col = 1, path='./scripts/wallets.csv' ):
    #  row ['id','address','privateKey','publicKey',...]
    list = []
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(csv_file, None)
        for user in reader:
            if( (int(user[0]) >= row_f) and (int(user[0]) <= row_l) ):
                list.append( user[col] )
    return list
               
               
def get_account(row = 0, col = 2, path='./scripts/wallets.csv' ):
    # 要部署到测试网络不在本地，添加账户对象
    # config数据来自brownie-config.yaml
    if network.show_active() == "development":
        return accounts[0]
    else:
        readCSV( row )
        #  return accounts.add(config['wallets'][key])
        return accounts.add( readCSV(row,col,path) )
        
    #  return accounts.add(config['wallets']['PRIVATE_KEY_1'])

def main():
    account = get_account( 0 )
    print('account=', account)
    print( readCSV_list(0,9,1,'./scripts/2.csv'))
    print( readCSV_list(0,9,4,'./scripts/2.csv'))
    
