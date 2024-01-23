import importlib
import inspect
import os
import pkgutil
from collections.abc import Callable
from enum import Enum
from time import sleep


from tensortradesdk.clients.base_client import BaseClient
from tensortradesdk.clients.enums import PoolType, CurveType
from tensortradesdk.clients.exceptions import GraphQLClientGraphQLMultiError
from tensortradesdk.clients.input_types import PoolConfig


default_args = {
    "slug": "degods",
    "owner": "8aNhUxFBxKcM4HxBVeson2cPFFvEZeKWGLL2nyfQTtvj",
    "buyer": "8aNhUxFBxKcM4HxBVeson2cPFFvEZeKWGLL2nyfQTtvj",
    "seller": "2uTUbQkx9ErxbudkTwdsTpnR3rHGdGb6Hzj4JFtyArTH",
    "bidder": "H6CUeqhmxihU1Xmvkyp7vKQUX3vyhyJ74PyGn7xBjPFt",
    "taker": "H6CUeqhmxihU1Xmvkyp7vKQUX3vyhyJ74PyGn7xBjPFt",
    "mint": "9HoGwPVKKRxBN2si7rXbczgS5Q2eK51yvWKDfjeYF6aQ",
    "token_mints": "8h5qaBJxgaDYkt8GKbDtDGUDNbQCWyW5SFCCEnLK76Fe",
    "max_price_lamports": "2900000000",
    "price": "30000000000",
    "max_price": "30000000000",
    "min_price": "30000000000",
    "bid_state_address": "q2PyS3qtgQX5vU7PcH866or3ZgNjaF76Upq4M8q7zzB",
    "min_price_lamports": "5000000000",
    "lamports": "9000000000",
    "pair": "5tkbVFDyB1qt9WTaY2JipYXmbtfSjXr816p7pJowFr2U",
    "pool": "5yEpsbcaN4LmCF1qJ3Dn1L2GmS3fCHMLhfsQvacCy76U",
    "new_config": PoolConfig(
        pool_type=PoolType.NFT,
        curve_type=CurveType.LINEAR,
        delta="0",
        starting_price="8000000000",
        mm_compound_fees=False,
        mm_fee_bps=None,
    ),
    "config": PoolConfig(
        pool_type=PoolType.NFT,
        curve_type=CurveType.LINEAR,
        delta="0",
        starting_price="8000000000",
        mm_compound_fees=False,
        mm_fee_bps=None,
    ),
    "wallets": ["6VX7RA4eBh2viV5Eczu6ENenwsiG5fEX2h3Gz2XKxNxH"],
    "mint_to_buy": "D37oqdfuxkK9phPg8VhsJ4ZMK2TAdgJawR8bRZFAFQmf",
    "mint_to_sell": "FPT4bKd5z3LS5cDitEjtHmVQ4JnX3VTa9wF4ni6bpJcg",
    "margin_nr": 0,
    "math_counter": 0,
    "quantity": 1,
}




def pytest_generate_tests(metafunc):
    import_all_modules("tensortradesdk.clients")
    api_key = os.environ["TENSOR_API_KEY"]
    p = []
    ids = []
    for class_ in BaseClient.__subclasses__():
        instance = class_(api_key)
        for method_name in get_class_methods(class_):
            method = getattr(instance, method_name)
            arguments = get_method_arguments(method)
            args = []
            for arg_name, info in arguments.items():
                if arg_name == "self":
                    continue
                if info.get("type") != "POSITIONAL_OR_KEYWORD":
                    continue
                if info.get("default") is not None:
                    continue
                if type(enum := info.get("annotation")) == type(Enum):
                    args.append(list(enum)[0])
                else:
                    args.append(default_args.get(arg_name))
            p.append((method, tuple(args)))
            ids.append(f"{class_.__name__}__{method_name}")
    metafunc.parametrize("client_methods", p, ids=ids)


def test_methods(client_methods: [Callable, tuple]):
    method, args = client_methods
    try:
        method(*args)
    except GraphQLClientGraphQLMultiError:
        # we don't want to fail the test in case of input value issues
        pass
    finally:
        sleep(1)


def import_all_modules(package_name):
    package = importlib.import_module(package_name)
    for _, module_name, _ in pkgutil.iter_modules(package.__path__, package_name + "."):
        importlib.import_module(module_name)


def get_class_methods(cls):
    base_classes = list(cls.__bases__)
    own_methods = []
    for name, func in inspect.getmembers(cls, predicate=inspect.isfunction):
        if not any(hasattr(base, name) for base in base_classes):
            own_methods.append(name)
    return own_methods


def get_method_arguments(func):
    signature = inspect.signature(func)
    parameters = signature.parameters
    annotations = getattr(func, "__annotations__", {})
    args = {}
    for name, param in parameters.items():
        arg_info = {
            "default": param.default
            if param.default is not inspect.Parameter.empty
            else None,
            "type": str(param.kind),
            "annotation": annotations.get(name, None),
        }
        args[name] = arg_info
    return args
