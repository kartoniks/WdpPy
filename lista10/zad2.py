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

lamiglowka("ciacho + ciacho = nadwaga")
