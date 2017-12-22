from random import *

def ukladalne(ds, dw):
  for i in ds:
    if i not in dw:
      return False
    if dw[i]<ds[i]:
      return False
  return True

def slownikuj(slowo):
  d = {}
  for i in slowo:
    if i not in d:
      d[i] = 0
    d[i] += 1
  return d

def shuf_wej(wejscie):
  wejscie = list(wejscie)
  shuffle(wejscie)
  wejscie = "".join(wejscie)
  return wejscie
    
wejscie="Artur Derechowski"
wejscie=wejscie.lower()
wejscie=wejscie.replace(" ", "")
imie=slownikuj(wejscie)
kandydaci = []
#imie = "".join(imie)
print(wejscie)
for w in open("slowa.txt"):
  w=w.strip()
  s=slownikuj(w)
  if ukladalne(s,imie):
    kandydaci.append(w)
alfa={}
for w in kandydaci:
  alfa["".join(sorted(w))] = w
while(True):
  wejscie=shuf_wej(wejscie)
  space1=randint(2,len(wejscie)//2)
  space2=randint(space1+1,len(wejscie)-1)
  w1="".join(sorted(wejscie[:space1]) )
  w2="".join(sorted(wejscie[space1:space2]) )
  w3="".join(sorted(wejscie[space2:]) )
  print(w1,w2,w3)
  if w1 in alfa and w2 in alfa and w3 in alfa:
    print(alfa[w1],alfa[w2],alfa[w3])
    break
#print(alfa)




