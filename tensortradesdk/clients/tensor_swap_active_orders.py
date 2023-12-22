# Generated by ariadne-codegen
# Source: resources/ariadne_client_configs/market_data.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import CurveType, PoolType


class TensorSwapActiveOrders(BaseModel):
    tswap_orders: List["TensorSwapActiveOrdersTswapOrders"] = Field(alias="tswapOrders")


class TensorSwapActiveOrdersTswapOrders(BaseModel):
    address: str
    created_unix: Any = Field(alias="createdUnix")
    curve_type: CurveType = Field(alias="curveType")
    delta: Any
    mm_compound_fees: bool = Field(alias="mmCompoundFees")
    mm_fee_bps: Optional[int] = Field(alias="mmFeeBps")
    nfts_for_sale: List["TensorSwapActiveOrdersTswapOrdersNftsForSale"] = Field(
        alias="nftsForSale"
    )
    nfts_held: int = Field(alias="nftsHeld")
    owner_address: str = Field(alias="ownerAddress")
    pool_type: PoolType = Field(alias="poolType")
    sol_balance: Any = Field(alias="solBalance")
    starting_price: Any = Field(alias="startingPrice")
    buy_now_price: Optional[Any] = Field(alias="buyNowPrice")
    sell_now_price: Optional[Any] = Field(alias="sellNowPrice")
    stats_accumulated_mm_profit: Any = Field(alias="statsAccumulatedMmProfit")
    stats_taker_buy_count: int = Field(alias="statsTakerBuyCount")
    stats_taker_sell_count: int = Field(alias="statsTakerSellCount")
    taker_buy_count: int = Field(alias="takerBuyCount")
    taker_sell_count: int = Field(alias="takerSellCount")
    updated_at: Any = Field(alias="updatedAt")


class TensorSwapActiveOrdersTswapOrdersNftsForSale(BaseModel):
    onchain_id: str = Field(alias="onchainId")
