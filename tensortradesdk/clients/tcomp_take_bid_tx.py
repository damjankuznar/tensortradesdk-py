# Generated by ariadne-codegen
# Source: resources/ariadne_client_configs/transactions.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class TcompTakeBidTx(BaseModel):
    tcomp_take_bid_tx: "TcompTakeBidTxTcompTakeBidTx" = Field(alias="tcompTakeBidTx")


class TcompTakeBidTxTcompTakeBidTx(BaseModel):
    txs: List["TcompTakeBidTxTcompTakeBidTxTxs"]


class TcompTakeBidTxTcompTakeBidTxTxs(BaseModel):
    last_valid_block_height: Optional[int] = Field(alias="lastValidBlockHeight")
    tx: Optional[Any]
    tx_v_0: Any = Field(alias="txV0")
