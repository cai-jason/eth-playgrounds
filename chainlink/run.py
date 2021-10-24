import json
import os
from web3 import Web3, HTTPProvider

# Generated after running `01_deploy_price_consumer_v3.py`
contract_address = "0x6F629473450372267Bf4ec3b712122c0b545152A"

w3 = Web3(HTTPProvider("https://kovan.infura.io/v3/%s" % os.environ["WEB3_INFURA_PROJECT_ID"]))
compiled_contract = json.load(open("./build/contracts/PriceFeedConsumer.json"))
abi = compiled_contract["abi"]
contract = w3.eth.contract(abi=abi, address=contract_address)

latest_price = contract.functions.getLatestPrice().call()
print("Latest ETH Price:", latest_price)
