# Generated by ariadne-codegen
# Source: resources/ariadne_client_configs/transactions.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class TcompCancelCollBidTx(BaseModel):
    tcomp_cancel_coll_bid_tx: "TcompCancelCollBidTxTcompCancelCollBidTx" = Field(
        alias="tcompCancelCollBidTx"
    )


class TcompCancelCollBidTxTcompCancelCollBidTx(BaseModel):
    txs: List["TcompCancelCollBidTxTcompCancelCollBidTxTxs"]


class TcompCancelCollBidTxTcompCancelCollBidTxTxs(BaseModel):
    last_valid_block_height: Optional[int] = Field(alias="lastValidBlockHeight")
    tx: Optional[Any]
    tx_v_0: Any = Field(alias="txV0")


TcompCancelCollBidTx.model_rebuild()
TcompCancelCollBidTxTcompCancelCollBidTx.model_rebuild()
TcompCancelCollBidTxTcompCancelCollBidTxTxs.model_rebuild()
