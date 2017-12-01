s1 = input()
s2 = input()

def zle(s1,s2):
  slow={}
  for i in range(len(s1)):
    if s1[i] in slow.keys() and slow[s1[i]] != s2[i]:
      return True
    slow[s1[i]] = s2[i]
  return False

A={}
if s1 == s2:
  print("NONE")
elif zle(s1,s2):
  print("CAN'T")
else:
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      A[s1[i]]=s2[i]
  for k,v in A.items():
    print(k+"->"+v)
