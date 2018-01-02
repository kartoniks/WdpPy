def czypolski(wyr):
  for i in 'ĘęÓóĄąŚśŁłŻżŹźĆćŃń':
    if i in wyr:
      return True
  return False

def dlugosc(wyr):
  d=0  
  for lit in wyr:
    if lit in 'qwertyuiopQWERTYUIOPASDFGHJKLasdfghjklZXCVBNMzxcvbnm':
      d += 1
  return d   

def litery(wyr):
  pol=''
  for lit in wyr:
    if lit in 'qwertyuiopQWERTYUIOPASDFGHJKLasdfghjklZXCVBNMzxcvbnm':
      pol += lit
  return pol

w_naj = ''
w_ter = ''
slowa = {}
for s in open('slowa.txt'):
  s=s.strip()
  slowa[s] = 1
for w in open('lalka.txt'):
  w=w.strip()
  w=w.split(' ')
  for wyr in w:
    if czypolski(wyr) or litery(wyr) not in slowa:
      if dlugosc(w_ter)>dlugosc(w_naj):
        w_naj = w_ter
        print(w_naj)
        print(wyr)
      w_ter = ''
    else:
      w_ter += wyr
      w_ter += ' '

