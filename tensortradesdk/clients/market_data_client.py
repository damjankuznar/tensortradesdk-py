# Generated by ariadne-codegen
# Source: resources/ariadne_client_configs/market_data.graphql

from typing import Any, Dict, List, Optional, Union

from .active_listings_v_2 import ActiveListingsV2
from .base_client import BaseClient
from .base_model import UNSET, UnsetType
from .collection_stats import CollectionStats
from .collections_stats import CollectionsStats
from .enums import ActiveListingsSortBy
from .hade_swap_active_orders import HadeSwapActiveOrders
from .input_types import ActiveListingsCursorInputV2, ActiveListingsFilters
from .tcomp_bids import TcompBids
from .tensor_swap_active_orders import TensorSwapActiveOrders


def gql(q: str) -> str:
    return q


class MarketDataClient(BaseClient):
    def collections_stats(
        self,
        slugs: Union[Optional[List[str]], UnsetType] = UNSET,
        slugs_me: Union[Optional[List[str]], UnsetType] = UNSET,
        slugs_display: Union[Optional[List[str]], UnsetType] = UNSET,
        ids: Union[Optional[List[str]], UnsetType] = UNSET,
        sort_by: Union[Optional[str], UnsetType] = UNSET,
        page: Union[Optional[int], UnsetType] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        **kwargs: Any
    ) -> CollectionsStats:
        """Only available in API mode!"""
        query = gql(
            """
            query CollectionsStats($slugs: [String!], $slugsMe: [String!], $slugsDisplay: [String!], $ids: [String!], $sortBy: String, $page: Int, $limit: Int) {
              allCollections(
                slugs: $slugs
                slugsMe: $slugsMe
                slugsDisplay: $slugsDisplay
                ids: $ids
                sortBy: $sortBy
                page: $page
                limit: $limit
              ) {
                total
                collections {
                  id
                  slug
                  slugMe
                  slugDisplay
                  statsV2 {
                    currency
                    buyNowPrice
                    buyNowPriceNetFees
                    sellNowPrice
                    sellNowPriceNetFees
                    numListed
                    numMints
                    floor1h
                    floor24h
                    floor7d
                    sales1h
                    sales24h
                    sales7d
                    salesAll
                    volume1h
                    volume24h
                    volume7d
                    volumeAll
                  }
                  firstListDate
                  name
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "slugs": slugs,
            "slugsMe": slugs_me,
            "slugsDisplay": slugs_display,
            "ids": ids,
            "sortBy": sort_by,
            "page": page,
            "limit": limit,
        }
        response = self.execute(
            query=query,
            operation_name="CollectionsStats",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return CollectionsStats.model_validate(data)

    def collection_stats(self, slug: str, **kwargs: Any) -> CollectionStats:
        query = gql(
            """
            query CollectionStats($slug: String!) {
              instrumentTV2(slug: $slug) {
                id
                slug
                slugMe
                slugDisplay
                statsV2 {
                  currency
                  buyNowPrice
                  buyNowPriceNetFees
                  sellNowPrice
                  sellNowPriceNetFees
                  numListed
                  numMints
                  floor1h
                  floor24h
                  floor7d
                  sales1h
                  sales24h
                  sales7d
                  salesAll
                  volume1h
                  volume24h
                  volume7d
                  volumeAll
                }
                firstListDate
                name
              }
            }
            """
        )
        variables: Dict[str, object] = {"slug": slug}
        response = self.execute(
            query=query, operation_name="CollectionStats", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return CollectionStats.model_validate(data)

    def tensor_swap_active_orders(
        self, slug: str, **kwargs: Any
    ) -> TensorSwapActiveOrders:
        query = gql(
            """
            query TensorSwapActiveOrders($slug: String!) {
              tswapOrders(slug: $slug) {
                address
                createdUnix
                curveType
                delta
                mmCompoundFees
                mmFeeBps
                nftsForSale {
                  onchainId
                }
                nftsHeld
                ownerAddress
                poolType
                solBalance
                startingPrice
                buyNowPrice
                sellNowPrice
                statsAccumulatedMmProfit
                statsTakerBuyCount
                statsTakerSellCount
                takerBuyCount
                takerSellCount
                updatedAt
              }
            }
            """
        )
        variables: Dict[str, object] = {"slug": slug}
        response = self.execute(
            query=query,
            operation_name="TensorSwapActiveOrders",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return TensorSwapActiveOrders.model_validate(data)

    def hade_swap_active_orders(self, slug: str, **kwargs: Any) -> HadeSwapActiveOrders:
        query = gql(
            """
            query HadeSwapActiveOrders($slug: String!) {
              hswapOrders(slug: $slug) {
                address
                assetReceiver
                baseSpotPrice
                boxes {
                  mint {
                    onchainId
                  }
                }
                buyOrdersQuantity
                createdAt
                curveType
                delta
                feeBps
                fundsSolOrTokenBalance
                lastTransactedAt
                mathCounter
                pairType
              }
            }
            """
        )
        variables: Dict[str, object] = {"slug": slug}
        response = self.execute(
            query=query,
            operation_name="HadeSwapActiveOrders",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return HadeSwapActiveOrders.model_validate(data)

    def active_listings_v_2(
        self,
        slug: str,
        sort_by: ActiveListingsSortBy,
        filters: Union[Optional[ActiveListingsFilters], UnsetType] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        cursor: Union[Optional[ActiveListingsCursorInputV2], UnsetType] = UNSET,
        **kwargs: Any
    ) -> ActiveListingsV2:
        query = gql(
            """
            query ActiveListingsV2($slug: String!, $sortBy: ActiveListingsSortBy!, $filters: ActiveListingsFilters, $limit: Int, $cursor: ActiveListingsCursorInputV2) {
              activeListingsV2(
                slug: $slug
                sortBy: $sortBy
                filters: $filters
                limit: $limit
                cursor: $cursor
              ) {
                page {
                  endCursor {
                    str
                  }
                  hasMore
                }
                txs {
                  mint {
                    onchainId
                  }
                  tx {
                    sellerId
                    grossAmount
                    grossAmountUnit
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "slug": slug,
            "sortBy": sort_by,
            "filters": filters,
            "limit": limit,
            "cursor": cursor,
        }
        response = self.execute(
            query=query,
            operation_name="ActiveListingsV2",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return ActiveListingsV2.model_validate(data)

    def tcomp_bids(self, slug: str, **kwargs: Any) -> TcompBids:
        query = gql(
            """
            query TcompBids($slug: String!) {
              tcompBids(slug: $slug) {
                address
                amount
                createdAt
                field
                fieldId
                filledQuantity
                margin
                marginNr
                ownerAddress
                quantity
                solBalance
                target
                targetId
              }
            }
            """
        )
        variables: Dict[str, object] = {"slug": slug}
        response = self.execute(
            query=query, operation_name="TcompBids", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return TcompBids.model_validate(data)
