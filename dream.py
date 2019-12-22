pip install web3
#猜哈哈哈
#我运气不好，1000没有出现有钱的。
```from web3 import Web3
import random
from eth_account import Account
my_provider = Web3.HTTPProvider('https://ropsten.infura.io/v3/')
w3 = Web3(my_provider)
for i in range(1000):
    ran1=random.randint(13014930929276798462788259291331114569350850385340543581156060683276001566006,99494142213455306845553332520503842689348673068902186218410089381058027554392)
    pri=hex(ran1)[2:]
    account = Account().privateKeyToAccount(pri)
    add=account.address
    if(w3.eth.getBalance(add,'latest')!=0):
        print(pri)#账户有钱，自动print
    print(i)
```
