from unittest.mock import MagicMock

import base58
import pytest
from pytest_mock import MockFixture
from solders.keypair import Keypair

from tensortradesdk import solana
from tensortradesdk.clients.tcomp_list_tx import (
    TcompListTx,
    TcompListTxTcompListTx,
    TcompListTxTcompListTxTxs,
)
from tensortradesdk.solana import SolanaClient


@pytest.fixture
def random_bytes_hex() -> str:
    return (
        "336896381a5960fa51ad0fd066ace323c2cd147d06392a9feb5660e3a0540397a4f9c495257285d3fd8e32a5f55e3fab5a36ff83d3"
        "c4977a2a6a6f73206811d1"
    )


@pytest.fixture
def keypair(random_bytes_hex) -> Keypair:
    return Keypair.from_bytes(bytes.fromhex(random_bytes_hex))


@pytest.fixture
def private_key(keypair) -> str:
    return base58.b58encode(bytes(keypair)).decode("ascii")


@pytest.fixture
def solana_client(private_key: str) -> SolanaClient:
    return SolanaClient(network="devnet", private_key=private_key)


@pytest.fixture
def mock_send_transaction(mocker: MockFixture):
    return mocker.patch("tensortradesdk.solana.send_transaction")


@pytest.fixture
def tx_buffer_example() -> TcompListTx:
    return TcompListTx(
        tcomp_list_tx=TcompListTxTcompListTx(
            txs=[
                TcompListTxTcompListTxTxs(
                    last_valid_block_height=218617400,
                    tx={
                        "type": "Buffer",
                        "data": list(
                            b"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01"
                            b"\x00\x07\n\xa4\xf9\xc4\x95%r\x85\xd3\xfd\x8e2\xa5\xf5^?\xabZ6\xff\x83\xd3\xc4\x97z*jos h"
                            b"\x11\xd1\x10\xbb-\xca\xe7~f~\xb2\xa3\xe8\xba\x94K\x9d\x7f%\xac\x98\xabB\r\xa7\xdb\xf2O*+"
                            b"\xf2R\x1a,G\x16V~\x17\xad\n-\x91\xf6~#n\xca6\xfdg\xc7$\x1b@\xee\xdaiR\xf9#\xa0\x15\xb3Gt"
                            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x8b\xab\x0c\xaf\x9d\xcd\xfdv>\x9eN\xeb<X\x89W"
                            b"\xf0P\xde\xcbz\x8e\x1495?\xe5u`Pd\xb8\x98\x8b\x80\xeby5(i\xb2$t_Y\xdd\xbf\x8a&X\xca\x13"
                            b"\xdch\x81!&5\x1c\xae\x07\xc1\xa5\xa5\t*\x13\xee\x95\xc4\x1c\xba\x08\xa6\x7fZ\xc6~\x8d"
                            b"\xf7\xe1\xda\x11b^\x1dd\x13\x7f\x8fO#\x83\x03\x7f\x14\x03\x06Fo\xe5!\x172\xff\xec\xad"
                            b"\xbar\xc3\x9b\xe7\xbc\x8c\xe5\xbb\xc5\xf7\x12k,C\x9b:@\x00\x00\x00\x0b\xbc\x0f\xc0\xbbG"
                            b"\xca/t\xc4\x11.\x94\xab\x13\xcf\xa3\xc64\xe5\xdc\x17\xea\xcb\x03\xcd\x1a#\xcd~x|\x06\xb5"
                            b"\xef\xb1u\xd7\x804l\x18\xfaa\xf5\x88\x19\x0eY\x81\xc4f\x8de\x1dg\xads\xc3n1\x18\x0f\xdf0"
                            b"\xde\xc4u\xb2\xcf`1\xb0W\xf1\xa9Ld\xfe#\x02\x9b\x1e|^\xba\x07)\xce5Y\xc6q\x8e\x0b\x15"
                            b"\x03\x07\x00\t\x03\x88\x13\x00\x00\x00\x00\x00\x00\x07\x00\x05\x02\x80\x1a\x06\x00\t\x0b"
                            b"\x04\x00\x00\x01\x08\x06\x03\x05\t\x02\x00\x80\x016\xae\xc1C\x11)\x84&\x7f\x06\x00\x00"
                            b"\x00\x00\x00\x00\x7f\x06\x00\x00\xb4\xb5]V\x99\xb1<\x8e\xc90\x0e\x83\t\xdf&\xa6\xf2\xc19"
                            b"\x82\xfc'&#[\x80\xa6\x10\xebS9e\xfa\x95\xe2\\\x893\xbfp2\\\xa8#\xbd\"\x94\x1a\xf3\xa7x"
                            b"\xbd,\xe3\x91\x19\xfc\x1f\x81\x14#,\xca\xac\x8ex\xd7\xee\x05\xe7Y\xeb7z\x0f$-?\xc0|\xbd"
                            b"\xafh\xf5\x14)\xdf\xb8E\x87\x88]3\xa7[\x15\x00h\xf3\xc9a\x00\x00\x00\x00\x00\x00\x00"
                        ),
                    },
                    tx_v_0={
                        "type": "Buffer",
                        "data": list(
                            b"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80"
                            b"\x01\x00\x02\x04\xa4\xf9\xc4\x95%r\x85\xd3\xfd\x8e2\xa5\xf5^?\xabZ6\xff\x83\xd3\xc4"
                            b"\x97z*jos h\x11\xd1G\x16V~\x17\xad\n-\x91\xf6~#n\xca6\xfdg\xc7$\x1b@\xee\xdaiR\xf9#\xa0"
                            b"\x15\xb3Gt\x03\x06Fo\xe5!\x172\xff\xec\xad\xbar\xc3\x9b\xe7\xbc\x8c\xe5\xbb\xc5\xf7"
                            b"\x12k,C\x9b:@\x00\x00\x00\x06\xb5\xef\xb1u\xd7\x804l\x18\xfaa\xf5\x88\x19\x0eY\x81\xc4f"
                            b"\x8de\x1dg\xads\xc3n1\x18\x0f\xdf0\xde\xc4u\xb2\xcf`1\xb0W\xf1\xa9Ld\xfe#\x02\x9b\x1e|^"
                            b"\xba\x07)\xce5Y\xc6q\x8e\x0b\x15\x03\x02\x00\t\x03\x88\x13\x00\x00\x00\x00\x00\x00\x02"
                            b"\x00\x05\x02\x80\x1a\x06\x00\x03\x0b\x05\x00\x00\x04\x06\x07\x08\t\x03\x01\x00\x80\x016"
                            b"\xae\xc1C\x11)\x84&\x7f\x06\x00\x00\x00\x00\x00\x00\x7f\x06\x00\x00\xb4\xb5]V\x99\xb1<"
                            b"\x8e\xc90\x0e\x83\t\xdf&\xa6\xf2\xc19\x82\xfc'&#[\x80\xa6\x10\xebS9e\xfa\x95\xe2\\\x893"
                            b'\xbfp2\\\xa8#\xbd"\x94\x1a\xf3\xa7x\xbd,\xe3\x91\x19\xfc\x1f\x81\x14#,\xca\xac\x8ex\xd7'
                            b"\xee\x05\xe7Y\xeb7z\x0f$-?\xc0|\xbd\xafh\xf5\x14)\xdf\xb8E\x87\x88]3\xa7[\x15\x00h\xf3"
                            b"\xc9a\x00\x00\x00\x00\x00\x00\x00\x012\x17\x91\xff\xafo[?lTy8 \xf2\xf3\x99\x08c\x04"
                            b"\x80\\]\xfc\\d\xcf\xcb0\xae\xdcX\x06\x01.\x05/\x00\x01\x02\n"
                        ),
                    },
                )
            ]
        )
    )


def test_versioned_tx(
    solana_client: SolanaClient,
    tx_buffer_example: TcompListTx,
    mock_send_transaction: MagicMock,
    mocker: MockFixture,
):
    create_legacy_transaction_spy = mocker.spy(solana, "create_legacy_transaction")
    create_versioned_transaction_spy = mocker.spy(
        solana, "create_versioned_transaction"
    )

    solana_client.submit_tensor_transaction(tx_buffer_example)

    assert create_legacy_transaction_spy.call_count == 0
    assert create_versioned_transaction_spy.call_count == 1
    assert mock_send_transaction.call_count == 1


def test_legacy_tx(
    solana_client: SolanaClient,
    tx_buffer_example: TcompListTx,
    mock_send_transaction: MagicMock,
    mocker: MockFixture,
):
    create_legacy_transaction_spy = mocker.spy(solana, "create_legacy_transaction")
    create_versioned_transaction_spy = mocker.spy(
        solana, "create_versioned_transaction"
    )

    # remove version tx buffer
    del tx_buffer_example.tcomp_list_tx.txs[0].tx_v_0

    solana_client.submit_tensor_transaction(tx_buffer_example)

    assert create_legacy_transaction_spy.call_count == 1
    assert create_versioned_transaction_spy.call_count == 0
    assert mock_send_transaction.call_count == 1
