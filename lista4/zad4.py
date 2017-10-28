from random import *

def randperm(n):
  L=list(range(n))
  N=[]
  x=0
  for i in range(n):
    x=randint(0, n-i-1)
    N.append(L[x])
    L=L[:x]+L[x+1:]
  print(N)

def fast(n):
  L=list(range(n))
  for i in range(n-1,0,-1):
    x=randint(0,i)
    L[i],L[x]=L[x],L[i]
  return(L)
    
    



for i in range(5):
  print(fast(10))
print(fast(10**6))
