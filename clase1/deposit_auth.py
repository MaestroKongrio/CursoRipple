"""Example of how we can set up an escrow"""
from datetime import datetime
from time import sleep

from xrpl.account import get_balance
from xrpl.clients import JsonRpcClient
from xrpl.models import AccountObjects, CheckCreate, CheckCash, CheckCancel
from xrpl.transaction.reliable_submission import submit_and_wait
from xrpl.utils import datetime_to_ripple_time
from xrpl.wallet import generate_faucet_wallet
from xrpl.models.transactions import AccountSet
# References
# - https://xrpl.org/escrowcreate.html#escrowcreate
# - https://xrpl.org/escrowfinish.html#escrowfinish
# - https://xrpl.org/account_objects.html#account_objects

# Create a client to connect to the test network
client = JsonRpcClient("https://s.altnet.rippletest.net:51234")

# Creating two wallets to send money between
wallet1 = generate_faucet_wallet(client, debug=True)

depositAuth= AccountSet(account=wallet1.address, set_flag=9)
depositAuthResponse= submit_and_wait(depositAuth, client, wallet1)
print(depositAuthResponse)