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
#Using Ganache Link 
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

    # Creating a function that automates Ethereum
def generate_account(w3):
    """Create a Digital Wallet from a mnemonic seed phrase."""
    # Acessing the mnemonic phrase from the .env file"
    mnemonic = os.getenv("MNEMONIC") 
    
    # Creating Wallet object instance
    wallet = Wallet(mnemonic)
    
    # Deriving Ethereum private key
    private, public = wallet.derive_account("eth")
    
    # Converting private key into an Ethereum account 
    account = Account.privateKeyToAccount(private)
    
    # Return the account from the function
    return account 
    # Creating function that calls and converts the wei balance of the account in to ether 
def get_balance(w3, address):
    """Using an Ethereum account address access the balance of Ether."""
    # Getting balance of address in wei 
    wei_balance = w3.eth.get_balance(address)
    # Coverting Wei value to ether 
    ether = w3.fromwei(wei_balance, "ether") 
    # Return the value in ether 
    return ether 

def send_transaction(w3, account, receiver, ether):
    """Send an authorized and secure transaction."""
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)
    wei_value = w3.towei(ether, "ether")
    gas_estimate = w3.eth.estimateGas({"to": receiver, "from":account.address, "value": wei_value})
        raw_transaction = {
            "to" : receiver, 
            "from": account.address, 
            "value": wei_value, 
            "gas": gas_estimate, 
            "gasPrice": 0, 
            "nonce" :
        w3.eth.getTransactionCount(account.address)
         }
         signed_transaction = account.signTransaction(raw_transaction)

         return w3.eth.sendRawTransaction(signed_transaction.raw_transaction)
