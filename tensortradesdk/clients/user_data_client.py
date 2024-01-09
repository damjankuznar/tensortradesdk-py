# Generated by ariadne-codegen
# Source: resources/ariadne_client_configs/user_data.graphql

from typing import Any, Dict, List, Optional, Union

from .base_client import BaseClient
from .base_model import UNSET, UnsetType
from .enums import ActiveListingsSortBy
from .input_types import ActiveListingsCursorInputV2
from .user_active_listings_v_2 import UserActiveListingsV2
from .user_tcomp_bids import UserTcompBids
from .user_tensor_swap_orders import UserTensorSwapOrders


def gql(q: str) -> str:
    return q


class UserDataClient(BaseClient):
    def user_tensor_swap_orders(
        self, owner: str, **kwargs: Any
    ) -> UserTensorSwapOrders:
        """
        Fetch all TensorSwap active orders for a wallet.
        """
        query = gql(
            """
            query UserTensorSwapOrders($owner: String!) {
              userTswapOrders(owner: $owner) {
                pool {
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
            }
            """
        )
        variables: Dict[str, object] = {"owner": owner}
        response = self.execute(
            query=query,
            operation_name="UserTensorSwapOrders",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return UserTensorSwapOrders.model_validate(data)

    def user_active_listings_v_2(
        self,
        wallets: List[str],
        sort_by: ActiveListingsSortBy,
        cursor: Union[Optional[ActiveListingsCursorInputV2], UnsetType] = UNSET,
        limit: Union[Optional[int], UnsetType] = UNSET,
        slug: Union[Optional[str], UnsetType] = UNSET,
        **kwargs: Any
    ) -> UserActiveListingsV2:
        """
        Fetch all marketplace mint listings (TensorSwap, TComp, HyperSpace, ME, etc.) for a wallet.
        """
        query = gql(
            """
            query UserActiveListingsV2($wallets: [String!]!, $sortBy: ActiveListingsSortBy!, $cursor: ActiveListingsCursorInputV2, $limit: Int, $slug: String) {
              userActiveListingsV2(
                wallets: $wallets
                cursor: $cursor
                limit: $limit
                sortBy: $sortBy
                slug: $slug
              ) {
                page {
                  endCursor {
                    str
                  }
                  hasMore
                }
                txs {
                  tx {
                    txId
                    txAt
                    source
                    mintOnchainId
                    grossAmount
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "wallets": wallets,
            "sortBy": sort_by,
            "cursor": cursor,
            "limit": limit,
            "slug": slug,
        }
        response = self.execute(
            query=query,
            operation_name="UserActiveListingsV2",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return UserActiveListingsV2.model_validate(data)

    def user_tcomp_bids(self, owner: str, **kwargs: Any) -> UserTcompBids:
        """
        Fetch all TComp active bids for a wallet.
        """
        query = gql(
            """
            query UserTcompBids($owner: String!) {
              userTcompBids(owner: $owner) {
                bid {
                  address
                  amount
                  field
                  fieldId
                  filledQuantity
                  quantity
                  solBalance
                  target
                  targetId
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"owner": owner}
        response = self.execute(
            query=query, operation_name="UserTcompBids", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return UserTcompBids.model_validate(data)
