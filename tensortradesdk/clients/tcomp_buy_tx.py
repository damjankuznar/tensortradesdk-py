# Generated by ariadne-codegen
# Source: resources/ariadne_client_configs/transactions.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class TcompBuyTx(BaseModel):
    tcomp_buy_tx: "TcompBuyTxTcompBuyTx" = Field(alias="tcompBuyTx")


class TcompBuyTxTcompBuyTx(BaseModel):
    txs: List["TcompBuyTxTcompBuyTxTxs"]


class TcompBuyTxTcompBuyTxTxs(BaseModel):
    tx: Optional[Any]
    tx_v_0: Any = Field(alias="txV0")
    last_valid_block_height: Optional[int] = Field(alias="lastValidBlockHeight")
