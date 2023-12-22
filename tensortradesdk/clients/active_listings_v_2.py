# Generated by ariadne-codegen
# Source: resources/ariadne_client_configs/market_data.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class ActiveListingsV2(BaseModel):
    active_listings_v_2: "ActiveListingsV2ActiveListingsV2" = Field(
        alias="activeListingsV2"
    )


class ActiveListingsV2ActiveListingsV2(BaseModel):
    page: "ActiveListingsV2ActiveListingsV2Page"
    txs: List["ActiveListingsV2ActiveListingsV2Txs"]


class ActiveListingsV2ActiveListingsV2Page(BaseModel):
    end_cursor: Optional["ActiveListingsV2ActiveListingsV2PageEndCursor"] = Field(
        alias="endCursor"
    )
    has_more: bool = Field(alias="hasMore")


class ActiveListingsV2ActiveListingsV2PageEndCursor(BaseModel):
    str: str


class ActiveListingsV2ActiveListingsV2Txs(BaseModel):
    mint: "ActiveListingsV2ActiveListingsV2TxsMint"
    tx: "ActiveListingsV2ActiveListingsV2TxsTx"


class ActiveListingsV2ActiveListingsV2TxsMint(BaseModel):
    onchain_id: str = Field(alias="onchainId")


class ActiveListingsV2ActiveListingsV2TxsTx(BaseModel):
    seller_id: Optional[str] = Field(alias="sellerId")
    gross_amount: Optional[Any] = Field(alias="grossAmount")
    gross_amount_unit: Optional[str] = Field(alias="grossAmountUnit")
