# Reference

::: tensortradesdk.solana.SolanaClient

## Clients for interacting with Tensor.trade GraphQL

All clients extend `tensortradesdk.clients.base_client.BaseClient` and require Tensor.trade GraphQL api key to be 
passed in.

::: tensortradesdk.clients.base_client.BaseClient

Example:
```py
import os

from tensortradesdk.clients.collection_data_client import CollectionDataClient


api_key = os.environ["TENSOR_API_KEY"] 
client = CollectionDataClient(api_key)

client.collection_mints("collection_slug")
```



::: tensortradesdk.clients.collection_data_client.CollectionDataClient