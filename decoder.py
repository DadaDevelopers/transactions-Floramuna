import json


def read_varint(data, offset):
    prefix = data[offset]
    offset += 1

    if prefix < 0xfd:
        return prefix, offset

    if prefix == 0xfd:
        value = int.from_bytes(data[offset:offset + 2], "little")
        return value, offset + 2

    if prefix == 0xfe:
        value = int.from_bytes(data[offset:offset + 4], "little")
        return value, offset + 4

    value = int.from_bytes(data[offset:offset + 8], "little")
    return value, offset + 8


def decode_transaction(hex_string):
    data = bytes.fromhex(hex_string)
    offset = 0

    # Version
    version = int.from_bytes(data[offset:offset + 4], "little")
    offset += 4

    # Check for SegWit marker and flag
    marker = None
    flag = None
    segwit = False

    if data[offset] == 0x00 and data[offset + 1] != 0x00:
        marker = data[offset:offset + 1].hex()
        flag = data[offset + 1:offset + 2].hex()
        offset += 2
        segwit = True

    # Inputs
    input_count, offset = read_varint(data, offset)
    inputs = []

    for _ in range(input_count):
        txid_bytes = data[offset:offset + 32]
        offset += 32

        txid = txid_bytes[::-1].hex()

        vout = int.from_bytes(data[offset:offset + 4], "little")
        offset += 4

        script_length, offset = read_varint(data, offset)

        script_sig = data[offset:offset + script_length].hex()
        offset += script_length

        sequence = data[offset:offset + 4].hex()
        offset += 4

        inputs.append({
            "txid": txid,
            "vout": vout,
            "scriptSig": script_sig,
            "sequence": sequence
        })

    # Outputs
    output_count, offset = read_varint(data, offset)
    outputs = []

    for _ in range(output_count):
        amount = int.from_bytes(data[offset:offset + 8], "little")
        offset += 8

        script_length, offset = read_varint(data, offset)

        script_pubkey = data[offset:offset + script_length].hex()
        offset += script_length

        outputs.append({
            "amount": amount,
            "scriptPubKey": script_pubkey
        })

    # Witness data
    witness = []

    if segwit:
        for _ in range(input_count):
            item_count, offset = read_varint(data, offset)

            items = []

            for _ in range(item_count):
                item_length, offset = read_varint(data, offset)

                item = data[offset:offset + item_length].hex()
                offset += item_length

                items.append(item)

            witness.append(items)

    # Locktime
    locktime = int.from_bytes(data[offset:offset + 4], "little")
    offset += 4

    return {
        "version": version,
        "marker": marker,
        "flag": flag,
        "inputs": inputs,
        "outputs": outputs,
        "witness": witness,
        "locktime": locktime
    }


# Provided transaction
tx_hex = "0200000000010131811cd355c357e0e01437d9bcf690df824e9ff785012b6115dfae3d8e8b36c10100000000fdffffff0220a107000000000016001485d78eb795bd9c8a21afefc8b6fdaedf718368094c08100000000000160014840ab165c9c2555d4a31b9208ad806f89d2535e20247304402207bce86d430b58bb6b79e8c1bbecdf67a530eff3bc61581a1399e0b28a741c0ee0220303d5ce926c60bf15577f2e407f28a2ef8fe8453abd4048b716e97dbb1e3a85c01210260828bc77486a55e3bc6032ccbeda915d9494eda17b4a54dbe3b24506d40e4ff43030e00"


decoded = decode_transaction(tx_hex)

print(json.dumps(decoded, indent=2))