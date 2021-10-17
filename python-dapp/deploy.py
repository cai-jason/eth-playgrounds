import json
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract

sys.path.append('../eth-playgrounds')
from private_keys import DEV_MAINNET_PUBLIC_KEY, DEV_MAINNET_PRIVATE_KEY, MORALIS_PRIVATE_KEY

# web3.py instance
w3 = Web3(HTTPProvider("https://speedy-nodes-nyc.moralis.io/%s/eth/mainnet/archive" % MORALIS_PRIVATE_KEY))
print(w3.isConnected())

acct = w3.eth.account.privateKeyToAccount(DEV_MAINNET_PRIVATE_KEY)

# compile smart contract with truffle first
truffleFile = json.load(open('./build/contracts/greeter.json'))
abi = truffleFile['abi']
bytecode = truffleFile['bytecode']
contract = w3.eth.contract(bytecode=bytecode, abi=abi)

# building transaction
construct_txn = contract.constructor().buildTransaction({
	'from': acct.address,
	'nonce': w3.eth.get_transaction_count(acct.address),
	'gas': 1728712,
	'gasPrice': w3.toWei('21', 'gwei')
	})

signed = acct.signTransaction(construct_txn)
tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
print(tx_hash.hex())

tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print("Contract Deployed At:", tx_receipt['contractAddress'])