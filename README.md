# Tensor.trade Python SDK


## Examples

## Collection Data
Get data based on GraphQL queries that can be found in [Tensor.trade API docs](https://tensor-hq.notion.site/PUBLIC-Tensor-Trade-API-Docs-alpha-b18e1a196187473bac9b5d6de5b47032#23a79268ff6e46bcb2d7d176eb2066da) 
and are also available in [Tensor.trade Apollo Studio Explorer](https://studio.apollographql.com/public/Tensor-Trade-API/variant/current/explorer?collectionId=39d0b9d4-91d5-4e2e-a153-62adcde8db45&focusCollectionId=39d0b9d4-91d5-4e2e-a153-62adcde8db45).
### Mint
```python
import os

from tensortradesdk.clients.collection_data_client import CollectionDataClient


api_key = os.environ["TENSOR_API_KEY"]

collection_data_client = CollectionDataClient(api_key)
mint = collection_data_client.mint(mint="5gzsZDwaVERyKEpujPYfHkpvc7jMGvixZC5aJqAnEGEP")
print(mint)
# will print out (formatted for better legibility)
# mint=MintMint(
#   slug='05c52d84-2e49-4ed9-a473-b43cab41e777', 
#   tswap_orders=[], 
#   tensor_bids=[
#     MintMintTensorBids(
#       bidder='yfUkk7NmNmimdSdLA4gjnnKd2bYuSbDRYQFLww9bPeq', 
#       expiry=1733821085000, 
#       price='51240000000'
#     )
#   ], 
#   hswap_orders=[], 
#   active_listings=[
#     MintMintActiveListings(
#       mint=MintMintActiveListingsMint(onchain_id='5gzsZDwaVERyKEpujPYfHkpvc7jMGvixZC5aJqAnEGEP'), 
#       tx=MintMintActiveListingsTx(
#         seller_id='9bnVcN1ASN7Y4RLaE6XFmf4kiCYBA5vGMn37fEpVsCmV', 
#         gross_amount='111990000000', 
#         gross_amount_unit='SOL_LAMPORT'
#       )
#     )
#   ]
# )
```

## Transactions

### TComp listing
```python
import os

from tensortradesdk.clients.transactions_client import TransactionsClient
from tensortradesdk.solana import SolanaClient


api_key = os.environ["TENSOR_API_KEY"]

transactions_client = TransactionsClient(api_key)
tx_buffer = transactions_client.tcomp_list_tx(
    mint="5gzsZDwaVERyKEpujPYfHkpvc7jMGvixZC5aJqAnEGEP",
    owner="GkDpghsgrsJPcajN7pP9jAtDyfEoK2jxw9CLhZro6i59",
    price="420000000000",
)
print(tx_buffer)
# will print out (formatted for better legibility)
# tcomp_list_tx=TcompListTxTcompListTx(
#   txs=[
#     TcompListTxTcompListTxTxs(
#       last_valid_block_height=218440754, 
#       tx={
#         'type': 'Buffer', 
#         'data': [1, 0, 0, 0, 0, ...]
#       }
#     )
#   ]
# )

solana_client = SolanaClient(
    network="mainnet",
    private_key="<private_key>",
)
solana_client.submit_tensor_transaction(tx_buffer)
```


* Get Mint Active Listings, Bids AND/OR Active Orders
  * https://tensor-hq.notion.site/PUBLIC-Tensor-Trade-API-Docs-alpha-b18e1a196187473bac9b5d6de5b47032#9b74a8e37b5840e382bcb18ddbbb59ba
* List single NFT
  * https://tensor-hq.notion.site/PUBLIC-Tensor-Trade-API-Docs-alpha-b18e1a196187473bac9b5d6de5b47032#2627138c16ba470ea9db4d10440e0bd6


## Development

### Update GraphQL schema
Download the schema from: 
https://studio.apollographql.com/public/Tensor-Trade-API/variant/current/schema/sdl

> Currently not allowed to introspect schema so unable to automate the following.

To update the schema from Tensor.trade GraphQL API run the following command:
```bash
poetry run update_gql_schema
```

This currenlty errors with:
```json
{
  "errors": [
    {
      "message": "GraphQL introspection is not allowed by Apollo Server, but the query contained __schema or __type. To enable introspection, pass introspection: true to ApolloServer in production",
      "extensions": {
        "code": "GRAPHQL_VALIDATION_FAILED"
      }
    }
  ]
}
```


### Autogenerate clients
To autogenerate clients from GrapgQL queries run the following command:
```bash
poetry run generate_gql_clients
```

