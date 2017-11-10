from random import *

def only_one(L):
  K=[]
  for i in L:
    if not i in K:
      K.append(i)
  return K

print(only_one([1,2,3,1,2,3,8,2,2,2,9,9,4]))


