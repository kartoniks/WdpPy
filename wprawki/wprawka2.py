L=[9,1,2,3,4,5,0,6,7,8]


maxl=0
begi=0
for i in range(len(L)):
  last=L[i]
  cand=0
  for j in range(len(L)-i):
    if L[i+j]>last:
      cand+=1
      last=L[i+j]
  if cand>maxl:
    maxl=cand
    begi=i

print(L[begi], end='')
last=begi
for i in range(begi, len(L)):
  if L[i]>last:
    print(L[i],end='')
  last=L[i]
    
  










  
