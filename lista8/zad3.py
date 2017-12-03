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
  if ukladalne(slownikuj(w),imie):
    kandydaci.append(w)

print(len(kandydaci))
dobre=set()

test={}
for i in kandydaci:
  test[tuple(slownikuj(i))] = i
for i in kandydaci:
  d = tuple(dopelnienie(slownikuj(i), imie))
  if d in test and slownikuj(test[d]+i) == imie:
    if test[d]<i:
      dobre.add((test[d],i))
    else:
      dobre.add((i,test[d]))

print(dobre)
    
'''
for i in kandydaci:
  for j in kandydaci:
    if slownikuj(j) == dopelnienie(slownikuj(i),imie):
      if i<j:
        dobre.add((i,j))
      else:
        dobre.add((j,i))
print(dobre)
'''
