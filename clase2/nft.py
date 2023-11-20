from xrpl.transaction import submit_and_wait
from xrpl.models.transactions.nftoken_mint import NFTokenMint, NFTokenMintFlag
from xrpl.models.amounts import IssuedCurrencyAmount
from xrpl.wallet import generate_faucet_wallet
from xrpl.models.requests import AccountNFTs
from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
import xrpl

# Mint an NFT on the XRPL via a NFTokenMint transaction
# https://xrpl.org/nftokenmint.html#nftokenmint

# If you want to mint a NFT on an already existing account, enter in the seed. If not, an account will be provided
# Make sure the seed variable is empty "", if you want to use a brand new testing account
JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
client = JsonRpcClient(JSON_RPC_URL)

# Get issuer account credentials from the testnet faucet
print("Requesting address from the Testnet faucet...")
issuer_wallet = generate_faucet_wallet(client=client)
issuerAddr = issuer_wallet.address

print(f"\nIssuer Account: {issuerAddr}")
print(f"Seed: {issuer_wallet.seed}")

# Construct NFTokenMint transaction to mint 1 NFT
print(f"Minting a NFT...")
mint_tx = NFTokenMint(
    account=issuerAddr,
    nftoken_taxon=1,
    flags=[3,8],
    uri=xrpl.utils.str_to_hex("https://test-copec.cl/token/123")
)

# Sign mint_tx using the issuer account
mint_tx_response = submit_and_wait(transaction=mint_tx, client=client, wallet=issuer_wallet)
mint_tx_result = mint_tx_response.result

print(f"\n  Mint tx result: {mint_tx_result['meta']['TransactionResult']}")
print(f"     Tx response: {mint_tx_result}")

for node in mint_tx_result['meta']['AffectedNodes']:
    if "CreatedNode" in list(node.keys())[0]:
        print(f"\n - NFT metadata:"
              f"\n        NFT ID: {node['CreatedNode']['NewFields']['NFTokens'][0]['NFToken']}"
              f"\n  Raw metadata: {node}")



# Query the minted account for its NFTs
get_account_nfts = client.request(
    AccountNFTs(account=issuerAddr)
)

nft_int = 1
print(f"\n - NFTs owned by {issuerAddr}:")

nfts=[]

for nft in get_account_nfts.result['account_nfts']:
    print(f"\n{nft_int}. NFToken metadata:"
          f"\n    Issuer: {nft['Issuer']}"
          f"\n    NFT ID: {nft['NFTokenID']}"
          f"\n NFT Taxon: {nft['NFTokenTaxon']}")
    nfts.append(nft['NFTokenID'])
    nft_int += 1

print(nfts)

target_wallet= generate_faucet_wallet(client=client,debug=True)


sell_offer_tx=xrpl.models.transactions.NFTokenCreateOffer(
    account=issuer_wallet.address,
    nftoken_id=nfts[0],
    amount="13100000",
    destination=target_wallet.address,
    flags=1
)
print("oferta de venta")
response=xrpl.transaction.submit_and_wait(sell_offer_tx,client,issuer_wallet)
print(response.result)

# Burn the NFT via a NFTokenBurn transaction
burn_tx=xrpl.models.transactions.NFTokenBurn(
    account=issuer_wallet.address,
    nftoken_id=nfts[0],   
)

burn_tx_response = submit_and_wait(transaction=burn_tx, client=client, wallet=issuer_wallet)
print(f"\n  Burn tx result: {burn_tx_response.result['meta']['TransactionResult']}")