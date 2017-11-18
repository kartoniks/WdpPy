from math import *

def prime(n):
  for i in range(2, int(sqrt(n)+1)):
    if n%i==0:
      return False
  return True

def dzielniki(n):
  S=set()
  for i in range(2, int(sqrt(n))+1):
    if n%i==0:
      if prime(i):
        S.add(i)
      if prime(n//i):
        S.add(n//i)
  return S

print(dzielniki(30))
