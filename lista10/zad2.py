def lamiglowka(n):
  litery = set(n) - set("+-=*/ ")
  n = n.replace("=", "==")
  if len(litery) > 10:
    return None
  cyfry = set("0123456789")
  sprawdz(litery, cyfry, n)

def sprawdz(lit, cyf, wyr):
  if not lit:
    print(lit, cyf, wyr, eval(wyr))
    if eval(wyr):
      return wyr
    return None
  for c in cyf:
    if c not in wyr:
      cyf = cyf - {c}
      for l in lit:
        lit = lit - {l}
        for i in range(len(wyr)):
          if wyr[i] == l:
            wyr = wyr.replace(str(l), str(c))
        sprawdz(lit, cyf, wyr)




lamiglowka("send + more = money")

'''
def lamiglowka(n):
  litery = set(n) - set("+-=*/ ")
  n = n.replace("=", "-")
  if len(litery) > 10:
    return "Zbyt dużo różnych liter w podanej łamigłówce"
  liczby = "0123456789"
  def permutacje(L,x,Lw):
    if len(L) == x:
      slownik = dict(zip(litery,L))
      napis = n
      for i in range(len(napis)):
        if napis[i] in slownik:
          napis = napis.replace(napis[i],slownik[napis[i]])
      for i in range(len(napis)):
        if napis[i] == "0" and (i == 0 or napis[i-1] == " "):
          break
      if eval(napis) == 0:
        Lw.append(slownik)
        print(Lw)
    elif not len(Lw):
      for e in liczby:
        L2 = L[:]
        if e not in L2:
          L2.append(e)
          permutacje(L2,x,[])
  permutacje([],len(litery),[])
'''
