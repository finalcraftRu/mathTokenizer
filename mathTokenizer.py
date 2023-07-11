alphabet="0123456789ABBCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,!? "
def fromListToStr(words:list):
 text=""
 for word in words:
  text+=word
 return text
def splitText(text:str,length_part=3):
 text+=" "*(len(text)%length_part)
 parts=[]
 for _ in range(len(text)//length_part):
  parts.append(text[:length_part])
  text=text[length_part:]
 return parts
def roundSymbols(text:str,padding=3,letter=" "):
 if len(text)%padding:
  return text+(letter[0]*(padding-(len(text)%padding)))
 else:
  return text
def encode(alphabet:str,text:str,padding=10,length_part=3):
 encoded=[0]*padding
 for i in range(min(len(text)//length_part,len(encoded))):
  part=text[:length_part]
  code=1
  text=text[length_part:]
  for j in range(length_part):
   code+=alphabet.index(part[j])*(len(alphabet)**j)
  encoded[i]=code
 return encoded
def decode(alphabet:str,codes:list[int],length_part=3):
 decoded=""
 for code in codes:
  if code:
   code-=1
   part=""
   for i in range(length_part):
    part+=alphabet[(code//(len(alphabet)**i))%len(alphabet)]
   decoded+=part
 return decoded