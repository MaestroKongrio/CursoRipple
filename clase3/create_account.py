from stellar_sdk import Keypair, Server
import requests


pair = Keypair.random()
print(f"Secret: {pair.secret}")
# Secret: SCMDRX7A7OVRPAGXLUVRNIYTWBLCS54OV7UH2TF5URSG4B4JQMUADCYU
print(f"Public Key: {pair.public_key}")


response = requests.get(f"https://friendbot.stellar.org?addr={pair.public_key}")
if response.status_code == 200:
    print(f"SUCCESS! You have a new account :)")
else:
    print(f"ERROR! Response: \n{response.text}")

    

server = Server("https://horizon-testnet.stellar.org")
public_key = "GD4NB2FLQAN5JO7PKPGZJMNBDYQXVSNVC7DEIZMOL5WSNSBLEBUTEF5Q"
account = server.accounts().account_id(public_key).call()
for balance in account['balances']:
    print(f"Type: {balance['asset_type']}, Balance: {balance['balance']}")
