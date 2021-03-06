import json
import time
from private_keys import DEV_MAINNET_PRIVATE_KEY, DEV_MAINNET_PUBLIC_KEY, INFURA_PROJECT_ID
from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/%s" % INFURA_PROJECT_ID))
print(w3.isConnected())

acct = w3.eth.account.privateKeyToAccount(DEV_MAINNET_PRIVATE_KEY)

# Generated after calling `compile_and_deploy()`
contract_address = "0xF343fc8edBC58482ab505CfbF4e636D195E818DF"

truffleFile = json.load(open("./build/contracts/SoapBox.json"))
abi = truffleFile["abi"]
contract = w3.eth.contract(abi=abi, address=contract_address)

def step_1_compile_and_deploy():
	# Compile smart contract with truffle
	truffleFile = json.load(open("./build/contracts/SoapBox.json"))
	abi = truffleFile["abi"]
	bytecode = truffleFile["bytecode"]
	contract = w3.eth.contract(bytecode=bytecode, abi=abi)

	# Building transaction
	construct_txn = contract.constructor().buildTransaction({
		"from": acct.address,
		"nonce": w3.eth.get_transaction_count(acct.address),
		"gas": 1728712,
		"gasPrice": w3.toWei("21", "gwei")
	})

	signed = acct.sign_transaction(construct_txn)
	txn_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
	print(txn_hash)
	txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
	print("Contract Deployed At", txn_receipt["contractAddress"])


def step_2_send_ether_to_contract(amount_in_ether):
	amount_in_wei = w3.toWei(amount_in_ether, "ether")
	nonce = w3.eth.get_transaction_count(DEV_MAINNET_PUBLIC_KEY)
	
	txn = {
		"to": contract_address,
		"value": amount_in_wei,
		"gas": 2000000,
		"gasPrice": w3.toWei("40", "gwei"),
		"nonce": nonce,
		"chainId": 3 # Ropsten
	}
	signed_txn = acct.sign_transaction(txn)
	txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
	txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
	print("%s ether successfully sent to contract address" % amount_in_ether)


def step_3_check_whether_address_is_approved(address):
	is_approved = contract.functions.isApproved(address).call()
	print("address: %s is approved:", is_approved)


def step_4_broadcast_an_opinion(opinion):
	txn = contract.functions.broadcastOpinion(opinion).buildTransaction({
		'chainId': 3,
		'gas': 140000,
		'gasPrice': w3.toWei('40', 'gwei'),
		'nonce': w3.eth.get_transaction_count(DEV_MAINNET_PUBLIC_KEY)
	})
	signed_txn = acct.sign_transaction(txn)
	txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
	txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)

	processed_receipt = contract.events.OpinionBroadcast().processReceipt(txn_receipt)
	print("Processed receipt:", processed_receipt)

	print("Address %s broadcasted the opinion %s" % 
		(processed_receipt[0].args._soapboxer, processed_receipt[0].args._opinion)
	)


step_4_broadcast_an_opinion("mayonaise is an instrument")

