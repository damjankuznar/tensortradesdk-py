# Generated by ariadne-codegen
# Source: resources/schema.graphql

from enum import Enum


class ActiveListingsSortBy(str, Enum):
    LastSaleAsc = "LastSaleAsc"
    LastSaleDesc = "LastSaleDesc"
    ListedDesc = "ListedDesc"
    PriceAsc = "PriceAsc"
    PriceDesc = "PriceDesc"
    RankHrttAsc = "RankHrttAsc"
    RankHrttDesc = "RankHrttDesc"
    RankStatAsc = "RankStatAsc"
    RankStatDesc = "RankStatDesc"
    RankTeamAsc = "RankTeamAsc"
    RankTeamDesc = "RankTeamDesc"
    RankTnAsc = "RankTnAsc"
    RankTnDesc = "RankTnDesc"


class AirdropThreeSortBy(str, Enum):
    By7d = "By7d"
    ByTotal = "ByTotal"


class AttachDetachAction(str, Enum):
    ATTACH = "ATTACH"
    DETACH = "DETACH"


class BidsSortBy(str, Enum):
    PriceAsc = "PriceAsc"
    PriceDesc = "PriceDesc"


class CollectionMintsSortBy(str, Enum):
    LastSaleAsc = "LastSaleAsc"
    LastSaleDesc = "LastSaleDesc"
    ListedTimeDesc = "ListedTimeDesc"
    ListingPriceAsc = "ListingPriceAsc"
    ListingPriceDesc = "ListingPriceDesc"
    RankHrttAsc = "RankHrttAsc"
    RankHrttDesc = "RankHrttDesc"
    RankStatAsc = "RankStatAsc"
    RankStatDesc = "RankStatDesc"
    RankTeamAsc = "RankTeamAsc"
    RankTeamDesc = "RankTeamDesc"
    RankTnAsc = "RankTnAsc"
    RankTnDesc = "RankTnDesc"


class Currency(str, Enum):
    ETH_WEI = "ETH_WEI"
    SOL_LAMPORT = "SOL_LAMPORT"


class CurveType(str, Enum):
    EXPONENTIAL = "EXPONENTIAL"
    LINEAR = "LINEAR"
    XYK = "XYK"


class DataSource(str, Enum):
    ALPHA = "ALPHA"
    AUCTION_HOUSE = "AUCTION_HOUSE"
    BUBBLEGUM = "BUBBLEGUM"
    DIGITALEYEZ = "DIGITALEYEZ"
    DIGITALEYEZ_V2 = "DIGITALEYEZ_V2"
    ELIXIR = "ELIXIR"
    ELIXIR_COMPOSED = "ELIXIR_COMPOSED"
    HADESWAP = "HADESWAP"
    HYPERSPACE = "HYPERSPACE"
    MAGICEDEN = "MAGICEDEN"
    MAGICEDEN_AUCTION = "MAGICEDEN_AUCTION"
    MAGICEDEN_V2 = "MAGICEDEN_V2"
    ONCHAIN = "ONCHAIN"
    SMB = "SMB"
    SMB_V2 = "SMB_V2"
    SOLANART = "SOLANART"
    SOLSEA = "SOLSEA"
    SWAPSORIAN = "SWAPSORIAN"
    TCOMP = "TCOMP"
    TENSORBID = "TENSORBID"
    TENSORSWAP = "TENSORSWAP"
    TOKEN_METADATA = "TOKEN_METADATA"
    TROLL = "TROLL"
    TSTAKE = "TSTAKE"
    YAWWW = "YAWWW"


class DepositWithdrawAction(str, Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"


class HSwapCurveType(str, Enum):
    Exponential = "Exponential"
    Linear = "Linear"
    XYK = "XYK"


class HSwapPairType(str, Enum):
    LiquidityProvision = "LiquidityProvision"
    NftForToken = "NftForToken"
    TokenForNFT = "TokenForNFT"


class OrderSortBy(str, Enum):
    SellNowPriceDesc = "SellNowPriceDesc"


class PoolType(str, Enum):
    NFT = "NFT"
    TOKEN = "TOKEN"
    TRADE = "TRADE"


class ProfilePointsPeriod(str, Enum):
    AllTime = "AllTime"
    LastDay = "LastDay"
    LastWeek = "LastWeek"


class RaritySystem(str, Enum):
    Hrtt = "Hrtt"
    Stat = "Stat"
    Team = "Team"
    Tn = "Tn"


class Reaction(str, Enum):
    COUNTER = "COUNTER"
    REJECT = "REJECT"


class SignMsgType(str, Enum):
    LINK = "LINK"
    VERIFY = "VERIFY"


class SupportedMarketplace(str, Enum):
    CoralCube = "CoralCube"
    Elixir = "Elixir"
    Fractal = "Fractal"
    HadeSwap = "HadeSwap"
    HyperSpace = "HyperSpace"
    MagicEden = "MagicEden"
    OpenSea = "OpenSea"
    Solanart = "Solanart"
    SolanartAH = "SolanartAH"
    Swapsorian = "Swapsorian"
    TComp = "TComp"
    TensorSwap = "TensorSwap"
    Yawww = "Yawww"


class SwapSide(str, Enum):
    Maker = "Maker"
    Taker = "Taker"


class TCompField(str, Enum):
    NAME = "NAME"


class TCompTarget(str, Enum):
    ASSET_ID = "ASSET_ID"
    WHITELIST = "WHITELIST"


class TRollRewardType(str, Enum):
    NONE = "NONE"
    TCOMP_LISTING = "TCOMP_LISTING"
    TSWAP_LISTING = "TSWAP_LISTING"
    TSWAP_POOL = "TSWAP_POOL"


class TRollTransactionStatus(str, Enum):
    CONFIRMED = "CONFIRMED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    STALE = "STALE"


class TStakeAction(str, Enum):
    STAKE = "STAKE"
    UNSTAKE = "UNSTAKE"


class TokenStandard(str, Enum):
    FUNGIBLE = "FUNGIBLE"
    FUNGIBLE_ASSET = "FUNGIBLE_ASSET"
    NON_FUNGIBLE = "NON_FUNGIBLE"
    NON_FUNGIBLE_EDITION = "NON_FUNGIBLE_EDITION"
    PROGRAMMABLE_NON_FUNGIBLE = "PROGRAMMABLE_NON_FUNGIBLE"
    PROGRAMMABLE_NON_FUNGIBLE_EDITION = "PROGRAMMABLE_NON_FUNGIBLE_EDITION"


class TradeAction(str, Enum):
    ACCEPT = "ACCEPT"
    BID = "BID"
    BUY = "BUY"
    CANCEL = "CANCEL"
    DELIST = "DELIST"
    DEPOSIT = "DEPOSIT"
    ELIXIR_APPRAISE = "ELIXIR_APPRAISE"
    INIT_UPDATE_MINT_PROOF = "INIT_UPDATE_MINT_PROOF"
    LIST = "LIST"
    MARGIN_ATTACH = "MARGIN_ATTACH"
    MARGIN_CLOSE = "MARGIN_CLOSE"
    MARGIN_DEPOSIT = "MARGIN_DEPOSIT"
    MARGIN_DETACH = "MARGIN_DETACH"
    MARGIN_INIT = "MARGIN_INIT"
    MARGIN_WITHDRAW = "MARGIN_WITHDRAW"
    OTC_BUNDLED_MAKER_WITHDRAW = "OTC_BUNDLED_MAKER_WITHDRAW"
    OTC_BUNDLED_MAKE_OFFER = "OTC_BUNDLED_MAKE_OFFER"
    OTC_BUNDLED_TAKER_WITHDRAW = "OTC_BUNDLED_TAKER_WITHDRAW"
    OTC_BUNDLED_TAKE_OFFER = "OTC_BUNDLED_TAKE_OFFER"
    STAKE = "STAKE"
    SWAP_BUY_NFT = "SWAP_BUY_NFT"
    SWAP_BUY_SINGLE_LISTING = "SWAP_BUY_SINGLE_LISTING"
    SWAP_CLOSE_POOL = "SWAP_CLOSE_POOL"
    SWAP_DELIST = "SWAP_DELIST"
    SWAP_DEPOSIT_LIQ = "SWAP_DEPOSIT_LIQ"
    SWAP_DEPOSIT_NFT = "SWAP_DEPOSIT_NFT"
    SWAP_DEPOSIT_SOL = "SWAP_DEPOSIT_SOL"
    SWAP_EDIT_POOL = "SWAP_EDIT_POOL"
    SWAP_EDIT_SINGLE_LISTING = "SWAP_EDIT_SINGLE_LISTING"
    SWAP_EXCHANGE_NFT = "SWAP_EXCHANGE_NFT"
    SWAP_INIT_POOL = "SWAP_INIT_POOL"
    SWAP_LIST = "SWAP_LIST"
    SWAP_SELL_NFT = "SWAP_SELL_NFT"
    SWAP_WITHDRAW_LIQ = "SWAP_WITHDRAW_LIQ"
    SWAP_WITHDRAW_MM_FEE = "SWAP_WITHDRAW_MM_FEE"
    SWAP_WITHDRAW_NFT = "SWAP_WITHDRAW_NFT"
    SWAP_WITHDRAW_SOL = "SWAP_WITHDRAW_SOL"
    UNSTAKE = "UNSTAKE"
    WITHDRAW = "WITHDRAW"


class TransactionType(str, Enum):
    ADJUST_PRICE = "ADJUST_PRICE"
    AUCTION_CANCEL = "AUCTION_CANCEL"
    AUCTION_CREATE = "AUCTION_CREATE"
    AUCTION_PLACE_BID = "AUCTION_PLACE_BID"
    AUCTION_SETTLE = "AUCTION_SETTLE"
    CANCEL_BID = "CANCEL_BID"
    CREATE_MINT = "CREATE_MINT"
    DELIST = "DELIST"
    ELIXIR_APPRAISE = "ELIXIR_APPRAISE"
    ELIXIR_BUY_PNFT = "ELIXIR_BUY_PNFT"
    ELIXIR_COMPOSED_BUY_NFT = "ELIXIR_COMPOSED_BUY_NFT"
    ELIXIR_COMPOSED_SELL_NFT = "ELIXIR_COMPOSED_SELL_NFT"
    ELIXIR_FRACTIONALIZE = "ELIXIR_FRACTIONALIZE"
    ELIXIR_FUSE = "ELIXIR_FUSE"
    ELIXIR_POOL_DEPOSIT_FNFT = "ELIXIR_POOL_DEPOSIT_FNFT"
    ELIXIR_POOL_EXCHANGE_FNFT = "ELIXIR_POOL_EXCHANGE_FNFT"
    ELIXIR_POOL_WITHDRAW_FNFT = "ELIXIR_POOL_WITHDRAW_FNFT"
    ELIXIR_SELL_PNFT = "ELIXIR_SELL_PNFT"
    FAILED = "FAILED"
    LIST = "LIST"
    MARGIN_ATTACH = "MARGIN_ATTACH"
    MARGIN_CLOSE = "MARGIN_CLOSE"
    MARGIN_DEPOSIT = "MARGIN_DEPOSIT"
    MARGIN_DETACH = "MARGIN_DETACH"
    MARGIN_INIT = "MARGIN_INIT"
    MARGIN_WITHDRAW = "MARGIN_WITHDRAW"
    OTC_BUNDLED_MAKER_WITHDRAW = "OTC_BUNDLED_MAKER_WITHDRAW"
    OTC_BUNDLED_MAKE_OFFER = "OTC_BUNDLED_MAKE_OFFER"
    OTC_BUNDLED_TAKER_WITHDRAW = "OTC_BUNDLED_TAKER_WITHDRAW"
    OTC_BUNDLED_TAKE_OFFER = "OTC_BUNDLED_TAKE_OFFER"
    OTHER = "OTHER"
    PLACE_BID = "PLACE_BID"
    ROLL_COMMIT = "ROLL_COMMIT"
    ROLL_FULFILL_NONE = "ROLL_FULFILL_NONE"
    ROLL_FULFILL_REWARD = "ROLL_FULFILL_REWARD"
    ROLL_FULFILL_SOL = "ROLL_FULFILL_SOL"
    SALE_ACCEPT_BID = "SALE_ACCEPT_BID"
    SALE_BUY_NOW = "SALE_BUY_NOW"
    STAKE = "STAKE"
    SWAP_BUY_NFT = "SWAP_BUY_NFT"
    SWAP_BUY_SINGLE_LISTING = "SWAP_BUY_SINGLE_LISTING"
    SWAP_CLOSE_POOL = "SWAP_CLOSE_POOL"
    SWAP_DELIST = "SWAP_DELIST"
    SWAP_DEPOSIT_LIQ = "SWAP_DEPOSIT_LIQ"
    SWAP_DEPOSIT_NFT = "SWAP_DEPOSIT_NFT"
    SWAP_DEPOSIT_SOL = "SWAP_DEPOSIT_SOL"
    SWAP_EDIT_POOL = "SWAP_EDIT_POOL"
    SWAP_EDIT_SINGLE_LISTING = "SWAP_EDIT_SINGLE_LISTING"
    SWAP_INIT_POOL = "SWAP_INIT_POOL"
    SWAP_LIST = "SWAP_LIST"
    SWAP_SELL_NFT = "SWAP_SELL_NFT"
    SWAP_WITHDRAW_LIQ = "SWAP_WITHDRAW_LIQ"
    SWAP_WITHDRAW_MM_FEE = "SWAP_WITHDRAW_MM_FEE"
    SWAP_WITHDRAW_NFT = "SWAP_WITHDRAW_NFT"
    SWAP_WITHDRAW_SOL = "SWAP_WITHDRAW_SOL"
    TRANSFER = "TRANSFER"
    UNSTAKE = "UNSTAKE"
    UPDATE_MINT = "UPDATE_MINT"


class UserTxStatus(str, Enum):
    CONFIRMED = "CONFIRMED"
    FAILED = "FAILED"
    FINALIZED = "FINALIZED"
    PENDING = "PENDING"
