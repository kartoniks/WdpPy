from random import *

n=10
L=[randint(1,1000) for i in range(n)]

def quicksort(L):
  if len(L)<=1: return L
  piv = L[0]
  L1 = [i for i in L[1:] if i<piv]
  L2 = [i for i in L[1:] if i>=piv]
  #print(L, L1, L2)
  return quicksort(L1) + [piv] + quicksort(L2)

def partition(L):
  maks = len(L) - 1
  print(L[maks])
  sp = 0
  for i in range(len(L)-1):
    if L[i]<maks:
      sp+=1
    else:
      temp = L[i]
      L[i] = L[sp]
      L[sp] = temp
  return L

print(L)
L=partition(L)
print(L)
