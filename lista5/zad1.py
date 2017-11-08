def F(n):
  if n % 2 == 0:
    return n / 2
  else:
    return 3 * n + 1

def energ(a,l):
  if a == 1:
    return l
  return energ(F(a), l+1)

def anCol(a,b):
  avg=0
  maxe=0
  mine=9999999
  L=[]
  for i in range(a,b+1):
    e=energ(i,0)#czy mozna tutaj jakos pozbyc sie drugiego argumentu w funkcji??
    L.append(e)
    avg+=e
    if maxe < e:
      maxe = e
    if mine > e:
      mine = e
  avg/=(b+1-a)
  if len(L)%2 == 0:
    med = L[len(L)//2 -1] + L[len(L)//2]
  else:
    med = L[len(L)//2]
  print("srednia:", avg)
  print("mediana:", med)
  print("max:", maxe, "min:", mine)


anCol(1,10)
