from web3 import Web3

# Connect to Ganache local blockchain
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Ensure connection
if not w3.isConnected():
    print("Failed to connect to Ethereum network")
    exit()

# Set up contract details (Replace with your contract ABI and address)
contract_address = "0x5FbDB2315678afecb367f032d93F642f64180aa3"
abi = [
    {
        "constant": True,
        "inputs": [],
        "name": "get",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"name": "x", "type": "uint256"}],
        "name": "set",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

# Create contract instance
contract = w3.eth.contract(address=contract_address, abi=abi)

# Set default account (replace with your Ethereum address)
w3.eth.default_account = w3.eth.accounts[0]
