import json
from private_keys import DEV_MAINNET_PRIVATE_KEY, INFURA_PROJECT_ID
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract

# web3.py instance
w3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/%s" % INFURA_PROJECT_ID))
print(w3.isConnected())

acct = w3.eth.account.privateKeyToAccount(DEV_MAINNET_PRIVATE_KEY)

# Compile smart contract with truffle
truffleFile = json.load(open("./build/contracts/greeter.json"))
abi = truffleFile["abi"]
bytecode = truffleFile["bytecode"]
contract = w3.eth.contract(bytecode=bytecode, abi=abi)

# Building transaction
construct_txn = contract.constructor().buildTransaction({
	"from": acct.address,
	"nonce": w3.eth.get_transaction_count(acct.address),
	"gas": 1728712,
	"gasPrice": w3.toWei('21', 'gwei')
})

signed = acct.sign_transaction(construct_txn)

tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
print(tx_hash.hex())
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Contract Deployed At:", tx_receipt["contractAddress"])