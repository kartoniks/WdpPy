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

def dopelnienie(ds, dw):
  dop={}
  for k in dw:
    if k not in ds:
      dop[k]=dw[k]
    elif ds[k]<dw[k]:
      dop[k]=dw[k]-ds[k]
  return dop

wejscie="Jan Nowakowski"
wejscie=wejscie.lower()
wejscie=wejscie.replace(" ", "")
imie=slownikuj(wejscie)
kandydaci = []
for w in open("slowa.txt"):
  w=w.strip()
  s=slownikuj(w)
  if ukladalne(s,imie):
    kandydaci.append(w)

test={}
for i in kandydaci:
  for j in kandydaci:
    
print(dobre)
   
