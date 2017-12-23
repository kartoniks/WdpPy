def potegowy(L):
  #print(L)
  if L == []:
    return [ 0 ]
  x=potegowy(L[1:])
  #print(x)
  return [ L[0] + i for i in x] + x

print(sorted(potegowy([1,2,3,100]) ))

'''
def nima(n,a,b):
  if n==0:
    return [ [] ]
  x=nima(n-1,a,b)
  wynik=[]
  for ciag in x:
    for i in range(a,b+1):
      if ciag == [] or i<=ciag[0]:
        wynik.append([i]+ciag)
  return wynik
'''
def nima(n,a,b):
  if n==0:
    return [ [] ]
  x=nima(n-1,a,b)
  return [[i]+ciag for i in range(a,b+1) for ciag in x if ciag==[] or i<=ciag[0]]

print(nima(3,10,12))


