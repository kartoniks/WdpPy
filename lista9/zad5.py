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
  
def nowe(s, d={}):
  t={}
  for i in s:
    if i in t: return False
    t[i]=1
    if i in d: return False
  return True
'''
def zlicz():
  trud={}
  for i in "qwertyuiopasdfghjklzxcvbnmęóąśłżźćń":
    trud[i]=100
  for i in range(100):
    s=losuj(slowa)
    for w in s:
      for j in w:
        if j in trud:
          trud[j]-=1
    print(i)
  print(trud)
'''
def dodaj(s,d):
  for a in s:
    if a not in d:
      d[a]=1
  return d

slowa=[]
for w in open("slowa.txt"):
  w=w.strip().lower()
  if nowe(w):
    slowa.append(w)
print(len(slowa))

d={}
w=slowa[randint(0,len(slowa)-1)]
d=dodaj(w,d)
print(d,w)














