"""Example of how we can set up an escrow"""
from datetime import datetime
from time import sleep

from xrpl.account import get_balance
from xrpl.clients import JsonRpcClient
from xrpl.models import AccountObjects, CheckCreate, CheckCash, CheckCancel
from xrpl.transaction.reliable_submission import submit_and_wait
from xrpl.utils import datetime_to_ripple_time
from xrpl.wallet import generate_faucet_wallet

# References
# - https://xrpl.org/escrowcreate.html#escrowcreate
# - https://xrpl.org/escrowfinish.html#escrowfinish
# - https://xrpl.org/account_objects.html#account_objects

# Create a client to connect to the test network
client = JsonRpcClient("https://s.altnet.rippletest.net:51234")

# Creating two wallets to send money between
wallet1 = generate_faucet_wallet(client, debug=True)
wallet2 = generate_faucet_wallet(client, debug=True)

depositAuth= 

# Both balances should be zero since nothing has been sent yet
print("Balances of wallets before Escrow tx was created:")
print(get_balance(wallet1.address, client))
print(get_balance(wallet2.address, client))

# Create a finish time (8 seconds from last ledger close)
finish_after = datetime_to_ripple_time(datetime.now()) + 8

# Create an EscrowCreate transaction, then sign, autofill, and send it
create_tx = CheckCreate(
    account=wallet1.address,
    destination=wallet2.address,
    send_max="1000000",
    destination_tag=122333
)

create_check_response = submit_and_wait(create_tx, client, wallet1)



nodes= create_check_response.result['meta']['AffectedNodes']


# Create an AccountObjects request and have the client call it to see if escrow exists
account_objects_request = AccountObjects(account=wallet1.address)
account_objects = (client.request(account_objects_request)).result["account_objects"]

print("Check object exists in wallet1's account:")
print(account_objects)

print("Delay")
sleep(6)

# Create an EscrowFinish transaction, then sign, autofill, and send it
finish_tx = CheckCash(
    amount="60000",
    account=wallet2.address,
    check_id=account_objects[0]['index'],
)

submit_and_wait(finish_tx, client, wallet2)

# If escrow went through successfully, 1000000 exchanged
print("Balances of wallets after check cashed:")
print(get_balance(wallet1.address, client))
print(get_balance(wallet2.address, client))