def lamiglowka(n):
  litery = set(n) - set("+-=*/ ")
  n = n.replace("=", "-")
  if len(litery) > 10:
    return None
  cyfry = "0123456789"
  def permutacje(L,x):
    global count    
    count += 1
    if len(L) == x:
      slow = dict(zip(litery,L))
      nap = n
      for i in range(len(nap)):
        if nap[i] in slow: 
          nap = nap.replace(nap[i], slow[nap[i]])
        if nap[i] == "0" and (i == 0 or nap[i-1] == " "):
          return None
      print(nap, count)
      if eval(nap) == 0:
        print(slow)
        return slow
    else:
      for e in cyfry:
        L2 = L[:]
        if e not in L2:
          L2.append(e)
          permutacje(L2,x)
  return permutacje([],len(litery))


count = 0
print(lamiglowka("ciacho + ciacho = nadwaga"))
