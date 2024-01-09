# Generated by ariadne-codegen
# Source: resources/schema.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    CurveType,
    DataSource,
    HSwapCurveType,
    HSwapPairType,
    ImmutableStatus,
    PoolType,
    RaritySystem,
    TCompField,
    TLockOrderStatus,
    TLockOrderType,
    TransactionType,
)


class ActiveListingsCursorInputV2(BaseModel):
    str: str


class ActiveListingsFilters(BaseModel):
    sources: Optional[List[DataSource]] = None
    prices: Optional["PriceFilter"] = None
    rarities: Optional["RarityFilter"] = None
    traits: Optional[List["TraitFilter"]] = None
    trait_count: Optional["TraitCountFilter"] = Field(alias="traitCount", default=None)
    name_filter: Optional[str] = Field(alias="nameFilter", default=None)
    owner_filter: Optional["OwnerFilter"] = Field(alias="ownerFilter", default=None)
    mints_filter: Optional[List[str]] = Field(alias="mintsFilter", default=None)
    currencies: Optional[List[Optional[str]]] = None


class AttributeInput(BaseModel):
    trait_type: str
    value: str


class BidsCursorInputV2(BaseModel):
    str: str


class CollectionMintsFilters(BaseModel):
    rarities: Optional["RarityFilter"] = None
    traits: Optional[List["TraitFilter"]] = None
    trait_count: Optional["TraitCountFilter"] = Field(alias="traitCount", default=None)
    name_filter: Optional[str] = Field(alias="nameFilter", default=None)
    only_listings: Optional[bool] = Field(alias="onlyListings", default=None)
    only_non_listings: Optional[bool] = Field(alias="onlyNonListings", default=None)
    listing_sources: Optional[List[DataSource]] = Field(
        alias="listingSources", default=None
    )
    listing_prices: Optional["PriceFilter"] = Field(alias="listingPrices", default=None)
    owner_filter: Optional["OwnerFilter"] = Field(alias="ownerFilter", default=None)
    mints_filter: Optional[List[str]] = Field(alias="mintsFilter", default=None)
    inscrip_filters: Optional["InscripFilter"] = Field(
        alias="inscripFilters", default=None
    )
    inscrip_order_filters: Optional[List["InscripOrderFilter"]] = Field(
        alias="inscripOrderFilters", default=None
    )
    currencies: Optional[List[Optional[str]]] = None


class HSwapModifyPairConfig(BaseModel):
    spot_price: Any = Field(alias="spotPrice")
    delta: Any
    fee_bps: Optional[int] = Field(alias="feeBps", default=None)


class HSwapPairConfig(BaseModel):
    spot_price: Any = Field(alias="spotPrice")
    delta: Any
    fee_bps: Optional[int] = Field(alias="feeBps", default=None)
    pair_type: HSwapPairType = Field(alias="pairType")
    curve_type: HSwapCurveType = Field(alias="curveType")


class InscripFilter(BaseModel):
    only_inscriptions: Optional[bool] = Field(alias="onlyInscriptions", default=None)
    immutable_status: Optional[ImmutableStatus] = Field(
        alias="immutableStatus", default=None
    )


class InscripOrderFilter(BaseModel):
    min: Optional[Any] = None
    max: Optional[Any] = None


class OwnerFilter(BaseModel):
    include: Optional[List[str]] = None
    exclude: Optional[List[str]] = None


class PoolConfig(BaseModel):
    pool_type: PoolType = Field(alias="poolType")
    curve_type: CurveType = Field(alias="curveType")
    starting_price: Any = Field(alias="startingPrice")
    delta: Any
    mm_compound_fees: Optional[bool] = Field(alias="mmCompoundFees", default=None)
    mm_fee_bps: Optional[int] = Field(alias="mmFeeBps", default=None)


class PriceFilter(BaseModel):
    min: Optional[Any] = None
    max: Optional[Any] = None


class RarityFilter(BaseModel):
    min: Optional[int] = None
    max: Optional[int] = None
    system: RaritySystem


class TCompBidFieldFilter(BaseModel):
    field: TCompField
    field_ids: List[str] = Field(alias="fieldIds")


class TCompBidsFilters(BaseModel):
    fields: Optional[List["TCompBidFieldFilter"]] = None
    no_fields: Optional[bool] = Field(alias="noFields", default=None)


class TLockCollectionsFilters(BaseModel):
    name: Optional[str] = None


class TLockFilters(BaseModel):
    statuses: Optional[List[TLockOrderStatus]] = None
    order_type: Optional[TLockOrderType] = Field(alias="orderType", default=None)
    taker: Optional[str] = None
    maker: Optional[str] = None


class TRollRequestedReward(BaseModel):
    odds_bps: int = Field(alias="oddsBps")
    type: str
    details: Optional["TRollRewardDetails"] = None


class TRollRewardDetails(BaseModel):
    address: str
    mint: str
    owner: str
    payment_mint: Optional[str] = Field(alias="paymentMint", default=None)
    token_standard: Optional[int] = Field(alias="tokenStandard", default=None)
    payment_base_amount: Any = Field(alias="paymentBaseAmount")
    royalty_bps: int = Field(alias="royaltyBps")


class TraitCountFilter(BaseModel):
    min: Optional[int] = None
    max: Optional[int] = None


class TraitFilter(BaseModel):
    trait_type: str = Field(alias="traitType")
    values: List[str]


class TransactionsCursorInput(BaseModel):
    tx_at: Any = Field(alias="txAt")
    tx_key: str = Field(alias="txKey")


class TransactionsFilters(BaseModel):
    tx_types: Optional[List[TransactionType]] = Field(alias="txTypes", default=None)
    mps: Optional[List[DataSource]] = None
    prices: Optional["PriceFilter"] = None
    traits: Optional[List["TraitFilter"]] = None
    trait_count: Optional["TraitCountFilter"] = Field(alias="traitCount", default=None)
    currencies: Optional[List[Optional[str]]] = None


class UserTxDataInput(BaseModel):
    version: int
    data: Any
