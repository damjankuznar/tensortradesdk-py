# Generated by ariadne-codegen
# Source: resources/ariadne_client_configs/transactions.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class TcompEditTx(BaseModel):
    tcomp_edit_tx: "TcompEditTxTcompEditTx" = Field(alias="tcompEditTx")


class TcompEditTxTcompEditTx(BaseModel):
    txs: List["TcompEditTxTcompEditTxTxs"]


class TcompEditTxTcompEditTxTxs(BaseModel):
    last_valid_block_height: Optional[int] = Field(alias="lastValidBlockHeight")
    tx: Optional[Any]
    tx_v_0: Any = Field(alias="txV0")


TcompEditTx.model_rebuild()
TcompEditTxTcompEditTx.model_rebuild()
TcompEditTxTcompEditTxTxs.model_rebuild()