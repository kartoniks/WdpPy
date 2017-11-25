def merge(l1,l2):
  k=[]
  while len(l1)!=0 or len(l2)!=0:
    print(l1,l2)
    if len(l1)==0:
      k+=l2
      l2=[]
    elif len(l2)==0:
      k+=l1
      l1=[]
    elif l1[0]<l2[0]:
      k.append(l1[0])
      del(l1[0])
    else:
      k.append(l2[0])
      del(l2[0])
  return k

def newt(n,k):
    





print()
