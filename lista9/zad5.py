from random import *


def losuj(s, d):
  l=[]
  while(len(d)<24):
    w=s[randint(0,len(s)-1)]
    #print(w,l,d)
    if nowe(w,d):
      for i in w:
        d[i]=1
      l.append(w)
  return l
  
def nowe(s, d):
  for i in s:
    if i in d: return False
  return True

def unik(s):
  t={}
  for i in s:
    if i in t: return False
    t[i]=1
  return True

def trudne(slowa):
  trud={}
  for i in range(100):
    d = losuj(slowa)
    for l in "qwertyuiopasdfghjklzxcvbnmęóąśłżźćń":
      if l not in d:
        if l not in trud:
          trud[l]=0
        trud[l] += 1
  return trud

def dodaj(s,d):
  for a in s:
    if a not in d:
      d[a]=1
  return d

def losuj(slowa):
  dobre=[]
  d={}
  w=slowa[randint(0,len(slowa)-1)]
  d=dodaj(w,d)
  dobre.append(w)
  #print(d,w)
  while( slowa != [] ):
    slowa2=[]
    for x in slowa:
      if nowe(x,d):
        slowa2.append(x)
    if len(slowa2) == 0:
      break
    w=slowa2[randint(0,len(slowa2)-1)]
    d=dodaj(w,d)
    dobre.append(w)
    #print(dobre)
    slowa=slowa2
  print(dobre)
  return d

slowa=[]
for w in open("slowa.txt"):
  w=w.strip().lower()
  if unik(w):
    slowa.append(w)
print(len(slowa))
trudne_litery = trudne(slowa)
print(trudne_litery)













