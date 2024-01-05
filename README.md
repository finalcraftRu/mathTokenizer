# MathTokenizer

## Overview

MathTokenizer is a simple Python module that provides functions for encoding and decoding text using a specified alphabet. The module includes functions for converting a list of words to a string, splitting a text into parts, rounding the length of symbols, encoding text into a list of numeric codes, and decoding numeric codes back into the original text.

## Usage

### Installation

To use MathTokenizer, simply include the provided `mathTokenizer.py` file in your project or import the functions directly into your script.

```python
from mathTokenizer import fromListToStr, splitText, roundSymbols, encode, decode
```

### Functions

#### `fromListToStr(words: list) -> str`

Converts a list of words into a single string.

#### `splitText(text: str, length_part: int = 3) -> list`

Splits a text into parts of a specified length. The text is padded with spaces if needed.

#### `roundSymbols(text: str, padding: int = 3, letter: str = " ") -> str`

Rounds the length of symbols in the text by padding with a specified letter.

#### `encode(alphabet: str, text: str, padding: int = 10, length_part: int = 3) -> list[int]`

Encodes a text using a specified alphabet into a list of numeric codes. The result is padded to the specified length.

#### `decode(alphabet: str, codes: list[int], length_part: int = 3) -> str`

Decodes a list of numeric codes back into the original text using a specified alphabet.

## Example

```python
alphabet = "0123456789ABBCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,!? "
text_to_encode = "Hello, World!"
encoded_codes = encode(alphabet, text_to_encode)
decoded_text = decode(alphabet, encoded_codes)

print(f"Original Text: {text_to_encode}")
print(f"Encoded Codes: {encoded_codes}")
print(f"Decoded Text: {decoded_text}")
```
