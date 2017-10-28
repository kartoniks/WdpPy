import math


def prime(n):
  for i in range(2,int(math.sqrt(n)+1)):
    if n%i==0:
      return 0
  return 1

def happy(n,sevens):
  if('7'*sevens in str(n)):
    return 1
  else:
    return 0


def znajdz(n,s):
  for i in range(int(math.pow(10,n)),1,-1):
    if(happy(i,s) and prime(i)):
      return i




print(znajdz(10,7))
