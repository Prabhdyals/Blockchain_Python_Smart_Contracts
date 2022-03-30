# Ethereum Account Functions

# Imports
import os 
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account 
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

#Creating a function that automates Ethereum
def generate_account(w3):
    """Create a Digital Wallet from a mnemonic seed phrase."""
    #Acessing the mnemonic phrase from the .env file"
    mnemonic = os.getenv("MNEMONIC") 
    
    # Creating Wallet object instance
    wallet = Wallet(mnemonic)
    
    #Deriving Ethereum private key
    private, public = wallet.derive_account("eth")
    
    #Converting private key into an Ethereum account 
    account = Account.privateKeyToAccount(private)
    
    #Return the account from the function
    return account 