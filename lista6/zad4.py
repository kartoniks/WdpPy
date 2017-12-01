def divid(s):
  p=0
  q=0
  L=[]
  while p<len(s):
    q=0
    if s[p] == ' ':
      p+=1
    else:
      while p+q<len(s) and s[p+q]!=' ':
        q+=1
      L.append(s[p:p+q])
      p=p+q+1
  return L

print(divid("  ala   ma  kota"))
