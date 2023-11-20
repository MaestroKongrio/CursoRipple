"""Example of how to handle partial payments"""
from xrpl.clients import JsonRpcClient
from xrpl.models import (
    AccountLines,
    IssuedCurrencyAmount,
    Payment,
    PaymentFlag,
    TrustSet,
)
from xrpl.transaction import submit_and_wait
from xrpl.wallet import generate_faucet_wallet

# Create a client to connect to the test network
client = JsonRpcClient("https://s.altnet.rippletest.net:51234")

# Creating two wallets to send money between
print("Generacion de las 3 wallets de ejemplo")
wallet1 = generate_faucet_wallet(client, debug=True)
wallet2 = generate_faucet_wallet(client, debug=True)
wallet3 = generate_faucet_wallet(client, debug=True)

#crear una trust line

trust_set_tx = TrustSet(
    account=wallet2.address,
    limit_amount=IssuedCurrencyAmount(
        currency="CLP",
        value="1000000",
        issuer=wallet1.address,
    ),
)

#en este caso, la wallet 2 esta entregando su confianza a la wallet 1 para que le envie CLP hasta un limite de 1.000.000
submit_and_wait(trust_set_tx, client, wallet2)

#crear una trust line
trust_set_tx_2 = TrustSet(
    account=wallet3.address,
    limit_amount=IssuedCurrencyAmount(
        currency="CLP",
        value="1000000",
        issuer=wallet1.address,
    ),
)   
result_trust_set_2= submit_and_wait(trust_set_tx_2, client, wallet3)




print("Saldos de Token CLP")
print((client.request(AccountLines(account=wallet1.address))).result["lines"])
print((client.request(AccountLines(account=wallet2.address))).result["lines"])
print((client.request(AccountLines(account=wallet3.address))).result["lines"])
# Create a Payment to send 3840 FOO from wallet1 (issuer) to destination (wallet2)
issue_quantity = "1000000"
payment_tx = Payment(
    account=wallet1.address,
    amount=IssuedCurrencyAmount(
        currency="CLP",
        value=issue_quantity,
        issuer=wallet1.address,
    ),
    destination=wallet2.address,
)
submit_and_wait(payment_tx, client, wallet1)

# Sign and autofill, then send transaction to the ledger
payment_response = submit_and_wait(payment_tx, client, wallet1)
print(payment_response)

print("Saldos de Token CLP")
print((client.request(AccountLines(account=wallet1.address))).result["lines"])
print((client.request(AccountLines(account=wallet2.address))).result["lines"])
print((client.request(AccountLines(account=wallet3.address))).result["lines"])


#intentamos hacer un pago desde la wallet 2 a la wallet 3
payment_tx_2 = Payment(
    account=wallet2.address,
    amount=IssuedCurrencyAmount(
        currency="CLP",
        value="100",
        issuer=wallet1.address,
    ),
    destination=wallet3.address,
)

second_payment_response = submit_and_wait(payment_tx_2, client, wallet2)

print("nuevos saldos")
print((client.request(AccountLines(account=wallet1.address))).result["lines"])
print((client.request(AccountLines(account=wallet2.address))).result["lines"])
print((client.request(AccountLines(account=wallet3.address))).result["lines"])