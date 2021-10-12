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
print("Ether balance:", my_ether_balance)

# Grab the latest block and pretty print it.
latest_block = w3.eth.get_block('latest')
latest_block_dict = dict(latest_block)
latest_block_json = json.loads(Web3.toJSON(latest_block_dict))
print(json.dumps(latest_block_json, indent=4, sort_keys=True))
