import sys
key = input()
val = input()


candidate = [[] for i in range(26)]

def check(candidate):
  for i in range(26):
    if len(candidate[i])>1:
      print("CAN'T")
      return True
  #for i in range(26):
  #  if len(candidate[i]) == 1 and candidate[i][0] != (chr(i+ord('A'))):
  #    print(chr(i+ord('A'))+"->"+candidate[i][0])

for i in range(len(key)):
  #if key[i] != val[i]:
  if val[i] not in candidate[ord(key[i])-ord('A')]: 
    candidate[ord(key[i])-ord('A')].append(val[i])

    
#for i in range(26):
#  print(candidate[i])
    

if key == val:
  print("NONE")
else:
  if not check(candidate):
    for i in range(len(key)):
      if key[i] != val[i]:
        print(key[i]+"->"+val[i])
