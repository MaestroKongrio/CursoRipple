from stellar_sdk import Asset, Keypair, Network, Server, TransactionBuilder
from stellar_sdk.exceptions import NotFoundError, BadResponseError, BadRequestError

secret_key_sender="SCHD2ZUA77YMTDSABME47MHIDNJYPKTAXHD6YZXXSCBFRG2NBI7QWVRC"
secret_key_receiver="SDIC3ENEWFMMBSM6JADPSXXR6TUTWOD3QBJFOKOSCWAO6IRYSNEWDOFC"

server = Server("https://horizon-testnet.stellar.org")
source_key = Keypair.from_secret(secret_key_sender)
destination_id = Keypair.from_secret(secret_key_receiver).public_key


source_account = server.load_account(source_key.public_key)

# Let's fetch base_fee from network
base_fee = server.fetch_base_fee()

# Start building the transaction.
transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
        # Especificamos el monto y la moneda del pago
        .append_payment_op(destination=destination_id, asset=Asset.native(), amount="100")
        # El memo es opcional, sirve como detalla
        .add_text_memo("Cuota Asado")
        .set_timeout(10)
        .build()
)

# Firmamos la transacción
transaction.sign(source_key)

try:
    # Envio a la red
    response = server.submit_transaction(transaction)
    print(f"Response: {response}")
except (BadRequestError, BadResponseError) as err:
    print(f"Something went wrong!\n{err}")