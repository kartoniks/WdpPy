def happy(n):
  s=str(n)
  if("777" in s):
    return 1
  else:
    return 0

def prime(n):
  for i in range(2,n//2):
    if(n%i==0):
      return 0
  return 1

c=0
for i in range(100000):
  if(happy(i) and prime(i)):
    c+=1

print(c)
