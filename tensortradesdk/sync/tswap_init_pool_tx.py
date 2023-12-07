# Generated by ariadne-codegen
# Source: resources/ariadne_client_configs/transactions.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class TswapInitPoolTx(BaseModel):
    tswap_init_pool_tx: "TswapInitPoolTxTswapInitPoolTx" = Field(
        alias="tswapInitPoolTx"
    )


class TswapInitPoolTxTswapInitPoolTx(BaseModel):
    pool: str
    txs: List["TswapInitPoolTxTswapInitPoolTxTxs"]


class TswapInitPoolTxTswapInitPoolTxTxs(BaseModel):
    last_valid_block_height: Optional[int] = Field(alias="lastValidBlockHeight")
    tx: Optional[Any]


TswapInitPoolTx.model_rebuild()
TswapInitPoolTxTswapInitPoolTx.model_rebuild()
TswapInitPoolTxTswapInitPoolTxTxs.model_rebuild()
