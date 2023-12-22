# Generated by ariadne-codegen
# Source: resources/ariadne_client_configs/transactions.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class TswapSellNftTx(BaseModel):
    tswap_sell_nft_tx: "TswapSellNftTxTswapSellNftTx" = Field(alias="tswapSellNftTx")


class TswapSellNftTxTswapSellNftTx(BaseModel):
    txs: List["TswapSellNftTxTswapSellNftTxTxs"]


class TswapSellNftTxTswapSellNftTxTxs(BaseModel):
    last_valid_block_height: Optional[int] = Field(alias="lastValidBlockHeight")
    tx: Optional[Any]
    tx_v_0: Any = Field(alias="txV0")
