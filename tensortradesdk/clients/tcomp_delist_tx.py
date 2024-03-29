# Generated by ariadne-codegen
# Source: resources/ariadne_client_configs/transactions.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class TcompDelistTx(BaseModel):
    tcomp_delist_tx: "TcompDelistTxTcompDelistTx" = Field(alias="tcompDelistTx")


class TcompDelistTxTcompDelistTx(BaseModel):
    txs: List["TcompDelistTxTcompDelistTxTxs"]


class TcompDelistTxTcompDelistTxTxs(BaseModel):
    last_valid_block_height: Optional[int] = Field(alias="lastValidBlockHeight")
    tx: Optional[Any]
    tx_v_0: Any = Field(alias="txV0")
