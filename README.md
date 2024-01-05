# Text Encoding and Decoding

This Python module provides a simple text encoding and decoding mechanism using a specified alphabet. The encoding process converts a given text into a list of codes, and the decoding process reverses this operation.

## Usage

1. **Define your Alphabet:**
    - The `alphabet` variable in the code represents the set of characters to be used. You can customize it as per your requirements.

2. **Encode Text:**
    - Use the `encode` function to convert a text into a list of codes.
    - Parameters:
        - `alphabet`: The set of characters used for encoding.
        - `text`: The input text to be encoded.
        - `padding` (optional): The length to which the encoded list should be padded.
        - `length_part` (optional): The length of each part into which the text is divided before encoding.

3. **Decode Codes:**
    - Use the `decode` function to convert a list of codes back into the original text.
    - Parameters:
        - `alphabet`: The set of characters used for encoding.
        - `codes`: The list of codes to be decoded.
        - `length_part` (optional): The length of each part into which the text was divided during encoding.

4. **Utility Functions:**
    - `fromListToStr`: Convert a list of words into a single string.
    - `splitText`: Split a text into parts of a specified length.
    - `roundSymbols`: Add padding to a text to make its length a multiple of a specified value.

## Example

```python
from encoding_module import *

# Define the alphabet
alphabet = "0123456789ABBCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,!? "

# Example text
input_text = "Hello, World!"

# Encode the text
encoded_text = encode(alphabet, input_text)

# Decode the codes
decoded_text = decode(alphabet, encoded_text)

print(f"Original Text: {input_text}")
print(f"Encoded Codes: {encoded_text}")
print(f"Decoded Text: {decoded_text}")
```

Feel free to customize the alphabet, text, and parameters according to your needs.

## Functions Overview

- **`encode`**
    - Converts a text into a list of codes using the specified alphabet.
- **`decode`**
    - Converts a list of codes back into the original text using the specified alphabet.
- **`fromListToStr`**
    - Converts a list of words into a single string.
- **`splitText`**
    - Splits a text into parts of a specified length.
- **`roundSymbols`**
    - Adds padding to a text to make its length a multiple of a specified value.

## Notes

- Make sure to keep the `alphabet` consistent when encoding and decoding texts.
- Adjust the optional parameters (`padding` and `length_part`) based on your specific use case.

Feel free to explore and integrate this module into your projects!
