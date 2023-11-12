from datetime import datetime
from time import sleep
from xrpl.wallet import Wallet
from xrpl.account import get_balance
from xrpl.clients import JsonRpcClient
from xrpl.models import AccountObjects, EscrowCreate, EscrowFinish
from xrpl.transaction.reliable_submission import submit_and_wait
from xrpl.utils import datetime_to_ripple_time, xrp_to_drops
from xrpl.wallet import generate_faucet_wallet
from xrpl.core.keypairs import derive_classic_address, derive_keypair, generate_seed
from xrpl.models.transactions import Payment

client = JsonRpcClient("https://s.altnet.rippletest.net:51234")

seed="sEdVwSoHz4q1dxNSZBjgpbCBMN5J4tg"
wallet1 = Wallet.from_seed(seed)

seed2= generate_seed()
print(seed2)
wallet2 = Wallet.from_seed(seed2)

print("Wallet Receptora " + wallet2.classic_address)

tiempo_cierre =  datetime_to_ripple_time(datetime.now()) + 60

my_tx_payment = Payment(
    account=wallet1.classic_address,
    amount=xrp_to_drops(20),
    destination=wallet2.classic_address,
)

tx_response = submit_and_wait(my_tx_payment, client, wallet1)


# Create an EscrowCreate transaction, then sign, autofill, and send it
create_tx = EscrowCreate(
    account=wallet1.address,
    destination=wallet2.address,
    amount=xrp_to_drops(30),
    finish_after=tiempo_cierre,
)

create_escrow_response = submit_and_wait(create_tx, client, wallet1)
print(create_escrow_response)

# Create an AccountObjects request and have the client call it to see if escrow exists
account_objects_request = AccountObjects(account=wallet1.address)
account_objects = (client.request(account_objects_request)).result["account_objects"]

print("Escrow object exists in wallet1's account:")
print(account_objects)

sleep(60)

finish_tx = EscrowFinish(
    account=wallet1.address,
    owner=wallet1.address,
    offer_sequence=create_escrow_response.result["Sequence"],
)

submit_and_wait(finish_tx, client, wallet2)
print("escrow finished")