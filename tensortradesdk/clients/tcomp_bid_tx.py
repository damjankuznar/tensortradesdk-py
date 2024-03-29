# Generated by ariadne-codegen
# Source: resources/ariadne_client_configs/transactions.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class TcompBidTx(BaseModel):
    tcomp_bid_tx: "TcompBidTxTcompBidTx" = Field(alias="tcompBidTx")


class TcompBidTxTcompBidTx(BaseModel):
    txs: List["TcompBidTxTcompBidTxTxs"]


class TcompBidTxTcompBidTxTxs(BaseModel):
    last_valid_block_height: Optional[int] = Field(alias="lastValidBlockHeight")
    tx: Optional[Any]
    tx_v_0: Any = Field(alias="txV0")
