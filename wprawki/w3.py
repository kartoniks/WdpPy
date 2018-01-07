import sys
import math

def isfree(x,y, b):
  for i in range(x):
    if b[i] == y or b[i]-i == y-x or b[i]+i == y+x:
      return False
  return True

def queens(n, b):
  b[0]=0
  k=1
  res=0
  while k>=0 and k<n:
    b[k]+=1
    while b[k]<n and not isfree(k, b[k],b):
      b[k]+=1      
    if b[k] < n:
      k+=1
    else:
      b[k]=-1
      k-=1
    if k==n:
      res+=1
      k-=1
  return res
      

n=int(input())
if n==1:
  print(1)
  sys.exit()
board = [-1]*n
print(queens(n,board))



