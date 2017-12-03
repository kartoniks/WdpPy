import random

def tlumacz(txt):
  wynik = []
  for p in txt.split():
    if p in pol_ang:
      wynik.append(najczestszy(pol_ang[p]))
    else:
      wynik.append('?' + p)
  return ' '.join(wynik)

def najczestszy(L):
  maks=0
  wyraz=""
  for i in L:
    if i in brown and maks<brown[i]:
      maks=brown[i]
      wyraz=i
  if maks == 0:
    return random.choice(L)
  return wyraz
         
pol_ang = {} # pusty słownik
brown = {}

for x in open('pol_ang.txt'):
  x = x.strip()
  L = x.split('=')
  if len(L) != 2:
    continue
  pol, ang = L
  
  if pol not in pol_ang:
    pol_ang[pol] = [ang]
  else:  
    pol_ang[pol].append(ang)

for w in open('brown.txt'):
  w = w.strip()
  L = w.split(' ')
  for i in L:
    if i not in brown:
      brown[i] = 0
    brown[i] += 1

zdanie = 'dziewczyna spotkać chłopiec i pójść do kino uerthf'

print (tlumacz(zdanie))
