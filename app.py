#Imports
import streamlit as st
from Ethereum_functions import generate_account
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))


#Importing functions from ethereum.py
account = generate_account(w3)

#Streamlit application headings
st.markdown("# Automating Ethereum with Streamlit!")
st.text("\n")
st.markdown("## Ethereum Account Address")

# Writing Ethereum account address to Streamlit
st.write(account.address)