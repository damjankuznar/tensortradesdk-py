# Generated by ariadne-codegen
# Source: resources/ariadne_client_configs/transactions.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class TswapBuyNftTx(BaseModel):
    tswap_buy_nft_tx: "TswapBuyNftTxTswapBuyNftTx" = Field(alias="tswapBuyNftTx")


class TswapBuyNftTxTswapBuyNftTx(BaseModel):
    txs: List["TswapBuyNftTxTswapBuyNftTxTxs"]


class TswapBuyNftTxTswapBuyNftTxTxs(BaseModel):
    last_valid_block_height: Optional[int] = Field(alias="lastValidBlockHeight")
    tx: Optional[Any]
    tx_v_0: Any = Field(alias="txV0")
