import mathTokenizer as mt

# Encode text to tokens
tokens = mt.encode(mt.alphabet, "Some text", 3, 3)
# tokens = [230074, 263542, 263066]
print(tokens)

# Encode tokens to text
text = mt.decode(mt.alphabet, [230074, 263542, 263066], 3)
# text = "Some text"
print(text)

# Split text to list of parts
texts = mt.splitText("HI", 1)
# texts = ["H", "I"]
print(texts)

# Merge parts to text
text = mt.fromListToStr(["H", "I"])
# text = "HI"
print(text)

# Round symbols
rounded = mt.roundSymbols("HI", 4, "#")
# rounded = "HI##"
print(rounded)