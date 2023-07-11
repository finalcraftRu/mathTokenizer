# mathTokenizer
Convert text to tokens by math
It very easy to use:
```python
import mathTokenizer as mt
tokens = mt.encode(mt.alphabet, "Hi", 1, 2)
print(tokens) # -> [3079]
```
Where 1 is padding; 2 is length of text`s part
mt.alphabet contains alphabet(surprise) which is "0123456789ABBCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,!? "
You can use your alphabet it can be str or list
it works with simple formula:
out = 1 + (letter at 0 pos * (alphabet ^ 0)) + (letter at 1 pos * (alphabet ^ 1))...
