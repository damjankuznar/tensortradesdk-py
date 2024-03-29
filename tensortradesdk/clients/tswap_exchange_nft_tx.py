# Generated by ariadne-codegen
# Source: resources/ariadne_client_configs/transactions.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class TswapExchangeNftTx(BaseModel):
    tswap_exchange_nft_tx: "TswapExchangeNftTxTswapExchangeNftTx" = Field(
        alias="tswapExchangeNftTx"
    )


class TswapExchangeNftTxTswapExchangeNftTx(BaseModel):
    txs: List["TswapExchangeNftTxTswapExchangeNftTxTxs"]


class TswapExchangeNftTxTswapExchangeNftTxTxs(BaseModel):
    last_valid_block_height: Optional[int] = Field(alias="lastValidBlockHeight")
    tx: Optional[Any]
    tx_v_0: Any = Field(alias="txV0")
