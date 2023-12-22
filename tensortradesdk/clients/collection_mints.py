# Generated by ariadne-codegen
# Source: resources/ariadne_client_configs/collection_data.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class CollectionMints(BaseModel):
    collection_mints_v_2: "CollectionMintsCollectionMintsV2" = Field(
        alias="collectionMintsV2"
    )


class CollectionMintsCollectionMintsV2(BaseModel):
    mints: List["CollectionMintsCollectionMintsV2Mints"]
    page: "CollectionMintsCollectionMintsV2Page"


class CollectionMintsCollectionMintsV2Mints(BaseModel):
    mint: "CollectionMintsCollectionMintsV2MintsMint"


class CollectionMintsCollectionMintsV2MintsMint(BaseModel):
    onchain_id: str = Field(alias="onchainId")
    rarity_rank_hr: Optional[int] = Field(alias="rarityRankHR")
    rarity_rank_tt: Optional[int] = Field(alias="rarityRankTT")


class CollectionMintsCollectionMintsV2Page(BaseModel):
    end_cursor: Optional[str] = Field(alias="endCursor")
    has_more: bool = Field(alias="hasMore")
