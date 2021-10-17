import json
from private_keys import DEV_MAINNET_PRIVATE_KEY, INFURA_PROJECT_ID
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract

# Compile smart contract with truffle
truffleFile = json.load(open("./build/contracts/greeter.json"))
abi = truffleFile["abi"]
bytecode = truffleFile["bytecode"]

# web3.py instance
w3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/%s" % INFURA_PROJECT_ID))
print(w3.isConnected())
contract_address = Web3.toChecksumAddress("0x6F629473450372267Bf4ec3b712122c0b545152A")
acct = w3.eth.account.privateKeyToAccount(DEV_MAINNET_PRIVATE_KEY)
acct_addr = acct.address

# Instantiate and deploy contract
contract = w3.eth.contract(abi=abi, bytecode=bytecode)
# Contract instance
contract_instance = w3.eth.contract(abi=abi, address=contract_address)

# Get txn receipt to get contract address
print('Contract value: {}'.format(contract_instance.functions.getGreeting().call()))