# Generated by ariadne-codegen
# Source: resources/ariadne_client_configs/market_data.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class CollectionsStats(BaseModel):
    all_collections: "CollectionsStatsAllCollections" = Field(alias="allCollections")


class CollectionsStatsAllCollections(BaseModel):
    total: int
    collections: List["CollectionsStatsAllCollectionsCollections"]


class CollectionsStatsAllCollectionsCollections(BaseModel):
    id: str
    slug: str
    slug_me: Optional[str] = Field(alias="slugMe")
    slug_display: Optional[str] = Field(alias="slugDisplay")
    stats_v_2: Optional["CollectionsStatsAllCollectionsCollectionsStatsV2"] = Field(
        alias="statsV2"
    )
    first_list_date: Optional[Any] = Field(alias="firstListDate")
    name: str


class CollectionsStatsAllCollectionsCollectionsStatsV2(BaseModel):
    currency: Optional[str]
    buy_now_price: Optional[Any] = Field(alias="buyNowPrice")
    buy_now_price_net_fees: Optional[Any] = Field(alias="buyNowPriceNetFees")
    sell_now_price: Optional[Any] = Field(alias="sellNowPrice")
    sell_now_price_net_fees: Optional[Any] = Field(alias="sellNowPriceNetFees")
    num_listed: int = Field(alias="numListed")
    num_mints: int = Field(alias="numMints")
    floor_1_h: Optional[float] = Field(alias="floor1h")
    floor_24_h: Optional[float] = Field(alias="floor24h")
    floor_7_d: Optional[float] = Field(alias="floor7d")
    sales_1_h: int = Field(alias="sales1h")
    sales_24_h: int = Field(alias="sales24h")
    sales_7_d: int = Field(alias="sales7d")
    sales_all: int = Field(alias="salesAll")
    volume_1_h: Any = Field(alias="volume1h")
    volume_24_h: Any = Field(alias="volume24h")
    volume_7_d: Any = Field(alias="volume7d")
    volume_all: Any = Field(alias="volumeAll")


CollectionsStats.model_rebuild()
CollectionsStatsAllCollections.model_rebuild()
CollectionsStatsAllCollectionsCollections.model_rebuild()
CollectionsStatsAllCollectionsCollectionsStatsV2.model_rebuild()
