##########################################
# Gra w życie (wersja graficzna)
##########################################

import kwadrat

kwadrat.tracer(0,10)

boardlen = 15

nieb = [list(w.strip()) for w in open('niebieskie.txt')]        
czer = [list(w.strip()) for w in open('czerwone.txt')]

for i in range(boardlen):
  for j in range(boardlen):
    if nieb[i][j] == '#':
      nieb[i][j] = 'N'
    if czer[i][j] == '#':
      czer[i][j] = 'C'

T=[]
for i in range(boardlen):
  T.append(nieb[i]+czer[i])
print(T)

def rysuj(T):
  kwadrat.clear()
  for y in range(len(T)):
    for x in range(len(T[y])):
      if T[y][x] == 'N':
        kolor = 'blue'
      if T[y][x] == 'C':
        kolor = 'red'
      if T[y][x] == '.':
        kolor = 'white'
      kwadrat.kwadrat(x, y, kolor)
  kwadrat.update()    

def sasiedzi(x,y):
  wynik = []
  for dx,dy in [ (-1,-1), (-1, 1), (1,-1), (1,1), (0,-1), (0,1), (1,0), (-1,0)]:
    nx = (x + dx) % MX
    ny = (y + dy) % MY
    wynik.append( (nx, ny) )
  return wynik
      
MY = len(T)    
MX = len(T[0])
    
def pusta_tablica():
  return [ MX * ['.'] for i in range(MY)]

def nowe_pokolenie(T):
  P = pusta_tablica()
  for y in range(MY):
    for x in range(MX):
      s_nieb = 0
      s_czer = 0
      for nx,ny in sasiedzi(x,y):
        if T[ny][nx] == 'N':
          s_nieb += 1
        if T[ny][nx] == 'C':
          s_czer +=1
      if T[y][x] != '.' and s_nieb+s_czer in [2,3]:
        P[y][x] = T[y][x]
      elif T[y][x] == '.' and s_nieb + s_czer == 3:
        if s_nieb>s_czer:
          P[y][x] = 'N'
        else:
          P[y][x] = 'C'       
  return P 

def liczba(tabela,znak):
  ile = 0  
  for x in tabela:
    for z in x:
      if z == znak:
        ile += 1
  return ile

licznik = 0
historia = set()  
  
while True:
  licznik += 1
  rysuj(T)
  T = nowe_pokolenie(T)
  if str(T) in historia:
    print ('koniec:', licznik)
    break
  if liczba(T, 'N') == 0:
    print('wygraly czerwone, liczba tur: ', licznik)
    break
  if liczba(T, 'C') == 0:
    print('wygraly niebieskie, liczba tur: ', licznik)
    break
  historia.add(str(T))
