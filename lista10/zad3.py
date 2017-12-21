def potegowy(L):
  #print(L)
  if L == []:
    return [ [] ]
  x=potegowy(L[1:])
  #print(x)
  return [ [L[0]] + i for i in x] + x

def sumy(L):
  res=[]
  for i in L:
    x=0
    for j in i:
      x+=j
    res+=[x]
  return sorted(set(res))

#print(potegowy([1,2,3]))
print(sumy(potegowy([1,2,3,100]) ))


