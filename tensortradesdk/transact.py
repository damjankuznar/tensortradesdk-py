from solana.transaction import Transaction
from solders.transaction import VersionedTransaction


def run_solana_transaction(client, sender_key_pair, transaction_buffer):
    transaction = Transaction.deserialize(bytes(transaction_buffer))
    transaction.sign(sender_key_pair)
    response = None
    try:
        response = client.send_transaction(transaction, sender_key_pair)
    except Exception as e:
        print("An error occurred:", e)
    return response


def run_solana_versioned_transaction(client, sender_key_pair, transaction_buffer):
    block = client.get_latest_blockhash().value
    transaction = VersionedTransaction.from_bytes(bytes(transaction_buffer))
    new_msg = MessageV0(
        transaction.message.header,
        transaction.message.account_keys,
        block.blockhash,
        transaction.message.instructions,
        []
    )
    signature = sender_key_pair.sign_message(to_bytes_versioned(new_msg))
    signed_tx = VersionedTransaction.populate(new_msg, [signature])
    response = None
    try:
        response = client.send_transaction(
            signed_tx
        )
    except Exception as e:
        print("An error occurred:", e)
    return response