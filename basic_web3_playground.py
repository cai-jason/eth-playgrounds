import json
from private_keys import MAINNET_PUBLIC_ADDR, MORALIS_PRIVATE_KEY
from web3 import Web3
from web3.providers.rpc import HTTPProvider

# Setup web3, connect to node.
eth_archive = "https://speedy-nodes-nyc.moralis.io/%s/eth/mainnet/archive" % MORALIS_PRIVATE_KEY
provider = HTTPProvider(eth_archive)
w3 = Web3(provider)

# Supply address, print ether balance.
my_address = MAINNET_PUBLIC_ADDR
my_wei_balance = w3.eth.get_balance(my_address)
my_ether_balance = Web3.fromWei(my_wei_balance, 'ether')
# print("Ether balance:", my_ether_balance)

# Grab the latest block and pretty print it.
latest_block = w3.eth.get_block('latest')
latest_block_dict = dict(latest_block)
latest_block_json = json.loads(Web3.toJSON(latest_block_dict))
# print(json.dumps(latest_block_json, indent=4, sort_keys=True))

# Look up block by number.
latest_block_hash = latest_block['hash']
latest_block_from_hash = w3.eth.get_block(latest_block_hash)
latest_block_from_hash_json = json.loads(Web3.toJSON(latest_block_from_hash))
# print(json.dumps(latest_block_from_hash_json, indent=4, sort_keys=True))

# Grab the latest block number.
latest_block_number = w3.eth.block_number
# print("Latest block number", latest_block_number)

# Query a transaction.
first_transaction_in_latest_block_addr = Web3.toHex(latest_block['transactions'][0])
first_transaction_in_latest_block = w3.eth.get_transaction(first_transaction_in_latest_block_addr)
first_transaction_in_latest_block_json = json.loads(Web3.toJSON(first_transaction_in_latest_block))
print(json.dumps(first_transaction_in_latest_block_json, indent=4, sort_keys=True))


