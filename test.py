# Define the network client
from xrpl.clients import JsonRpcClient
from xrpl.wallet import generate_faucet_wallet
from xrpl.models.transactions import Payment
from xrpl.utils import xrp_to_drops
from xrpl.transaction import submit_and_wait
from xrpl.models.requests.account_info import AccountInfo

JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
client = JsonRpcClient(JSON_RPC_URL)

# Create a wallet using the testnet faucet:
# https://xrpl.org/xrp-testnet-faucet.html

test_wallet = generate_faucet_wallet(client, debug=True)

print(test_wallet)

#obtenemos el estado de la cuenta
acct_info = AccountInfo(
    account=test_wallet.classic_address,
    ledger_index="validated",
    strict=True,
)


my_tx_payment = Payment(
    account=test_wallet.classic_address,
    amount=xrp_to_drops(22),
    destination="rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe",
)

tx_response = submit_and_wait(my_tx_payment, client, test_wallet)

print(tx_response)