from private_keys import MAINNET_PUBLIC_ADDR, MORALIS_PRIVATE_KEY
from web3 import Web3
from web3.providers.rpc import HTTPProvider

# Setup web3, connect to node.
eth_archive = "https://speedy-nodes-nyc.moralis.io/%s/eth/mainnet/archive" % MORALIS_PRIVATE_KEY
provider = HTTPProvider(eth_archive)
web3 = Web3(provider)

# Supply address, print ether balance
my_address = MAINNET_PUBLIC_ADDR
my_wei_balance = web3.eth.get_balance(my_address)
my_ether_balance = Web3.fromWei(my_wei_balance, 'ether')
print("Ether balance:", my_ether_balance)