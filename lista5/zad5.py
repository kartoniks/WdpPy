from random import randint

def generuj(n,l):
  for i in range(n):
    l[i]=randint(1,6)

def sprawdz1(n,l):
  for i in range(n-5):
    goodl=0
    for j in range(5):
      if l[j+i]>=l[j+i+1]:
        goodl+=1
      if goodl==5:
        return True
  return False

def sprawdz2(n,l):#jak zmienic operator w funkcji zeby te 2 funkcje zapisac jako jedna?
  for i in range(n-4):
    goodl=0
    for j in range(4):
      if l[j+i]<l[j+i+1]:
        goodl+=1
      if goodl==4:
        return True
  return False

l=[0]*100

rosnace,malejace = 0,0
proby=10000
for i in range(proby):
  generuj(100,l)
  if sprawdz1(100,l):
    malejace+=1
  if sprawdz2(100,l):
    rosnace+=1
print(malejace/proby, rosnace/proby)
