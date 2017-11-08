from random import *

def only_one(L):
  K=[]
  K2=[]
  for i in range(len(L)):
    K.append((L[i], i))
  K.sort()
  for i in range(len(K)):
    if K[i-1][0] != K[i][0]:
      K2.append(K[i])
  K2.sort(key = lambda x: x[1])# dlaczego nie key=1?
  
  K=[]
  for i in K2:
    K.append(i[0])
  return K



print(only_one([1,2,3,1,2,3,8,2,2,2,9,9,4]))
