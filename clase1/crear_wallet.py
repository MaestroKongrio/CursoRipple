from xrpl.wallet import Wallet
from xrpl.core.keypairs import derive_classic_address, derive_keypair, generate_seed
from xrpl.clients import JsonRpcClient
from xrpl.models import Ledger, Tx
from xrpl.account import get_balance, does_account_exist
from xrpl.models.transactions import Payment
from xrpl.utils import xrp_to_drops
from xrpl.transaction import submit_and_wait

# Generamos una nueva wallet
#seed= generate_seed()
seed="sEdVwSoHz4q1dxNSZBjgpbCBMN5J4tg"
print("Semilla Criptografica: " + seed)

wallet = Wallet.from_seed(seed)
print(wallet)

JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
client = JsonRpcClient(JSON_RPC_URL)

seed2= generate_seed()
print(seed2)
wallet2 = Wallet.from_seed(seed2)
