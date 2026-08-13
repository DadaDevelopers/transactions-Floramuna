````markdown
# Bitcoin Transaction Decoding Assignment

## Overview

This project implements a Bitcoin transaction decoder in Python.

The decoder accepts a raw Bitcoin transaction in hexadecimal format, parses its individual components, and produces structured transaction data.

The assignment also includes a manual decoding of the provided transaction.

---

## Assignment Tasks

### Task 1: Manual Transaction Decode

The provided SegWit transaction was manually decoded by identifying:

- Transaction version
- SegWit marker and flag
- Number of inputs
- Input transaction ID
- Previous output index
- Script length
- ScriptSig
- Sequence number
- Number of outputs
- Output amounts
- Output script lengths
- Output ScriptPubKeys
- Witness data
- Locktime

The manual decoding is documented in:

`manual-decode.md`

---

### Task 2: Transaction Decoder

A Python transaction decoder was implemented in:

`decoder.py`

The decoder:

1. Accepts a raw Bitcoin transaction in hexadecimal format.
2. Converts the hexadecimal transaction into bytes.
3. Reads the transaction version.
4. Detects SegWit transactions using the marker and flag.
5. Reads the input count.
6. Parses each transaction input.
7. Reads the output count.
8. Parses each transaction output.
9. Parses witness data for SegWit transactions.
10. Reads the transaction locktime.
11. Returns the decoded transaction as structured data.

---

## Files

```text
transactions-Floramuna/
│
├── manual-decode.md
├── decoder.py
├── output.txt
└── README.md
````

### `manual-decode.md`

Contains the manual breakdown of the provided Bitcoin transaction hexadecimal data.

### `decoder.py`

Contains the Python implementation of the Bitcoin transaction decoder.

### `output.txt`

Contains the output produced by running the decoder against the provided transaction.

### `README.md`

Contains documentation explaining the assignment and implementation.

---

## Transaction Tested

The decoder was tested using the transaction hexadecimal provided in the assignment.

The transaction is a SegWit transaction with:

* Version: `2`
* Marker: `00`
* Flag: `01`
* Input count: `1`
* Output count: `2`

The program successfully decoded the transaction and produced structured JSON output.

---

## Running the Decoder

Python 3 is required.

From the project directory, run:

```bash
python3 decoder.py
```

The decoded transaction will be printed to the terminal.

The resulting output is also stored in:

```text
output.txt
```

---

## Decoded Transaction Components

The decoder successfully identified the following components:

* Version
* SegWit marker
* SegWit flag
* Transaction inputs
* Previous transaction hash
* Previous output index
* ScriptSig
* Sequence
* Transaction outputs
* Output amounts in satoshis
* ScriptPubKeys
* Witness data
* Locktime

---

## Bitcoin Transaction Parsing

Bitcoin transactions use a binary serialization format. The decoder reads the transaction sequentially according to this format.

Important characteristics used by the decoder include:

* Little-endian byte order for integer fields
* Variable-length integers (VarInts)
* SegWit marker and flag
* Separate witness data
* Amounts represented in satoshis

For SegWit transactions, the marker `00` and flag `01` appear after the transaction version.

---

## Verification

The decoded transaction was checked against the transaction information supplied in the assignment.

The program output is stored in `output.txt`, while the manual parsing is documented separately in `manual-decode.md`.

---

## Conclusion

This assignment demonstrates how a raw Bitcoin transaction can be parsed from hexadecimal data into its individual transaction components.

It also demonstrates the difference between manually interpreting Bitcoin's serialized transaction format and implementing a program that performs the same parsing automatically.

```
```
