import os
from interface import ContractInterface
from private_keys import INFURA_PROJECT_ID
from web3 import Web3, HTTPProvider
from solcx import compile_standard, install_solc

install_solc("0.5.1")

# Initalize web3 object
# w3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/%s" % INFURA_PROJECT_ID))
w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))

# Create a path object to Solidity source files
contract_dir = os.path.abspath('./contracts/')

# Initialize interface
greeter_interface = ContractInterface(w3, 'Greeter', contract_dir)
# print(type(greeter_interface))

# Compile contracts
greeter_interface.compile_source_files()

# Deploy contracts
greeter_interface.deploy_contract()

instance = greeter_interface.get_instance()
print(instance.functions.greet().call())

