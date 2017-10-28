import math

def prime(n):
  for i in range(2,int(math.sqrt(n)+1)):
    if n%i==0:
      return 0
  return 1

def happy(n,sevens):
  if '7'*sevens in str(n):
    return 1
  else:
    return 0


def znajdz(n,s):
  for i in range(int(math.pow(10,n)),1,-1):
    if happy(i,s) and prime(i):
      return i

def genhap(n):
  L=[]
  for i in range(10):
    for j in range(10):
      for k in range(10):
          L.append(7777777000+100*i+10*j+k)
          L.append(i*10**9+777777700+10*j+k)
          L.append(i*10**9+j*10**8+77777770+k)
          L.append(i*10**9+j*10**8+k*10**7+7777777)
  L.sort()
  L=set(L)
  return L


L=genhap(10)
p=0
for i in L:
  if prime(int(i)):
    p+=1

print(p)

