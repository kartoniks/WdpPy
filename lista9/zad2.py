# Spełnianie formuł logicznych
####################################################
   
def ciagi_binarne(N):
  if N == 0:
    return [ [] ]
  return [ b + c for c in ciagi_binarne(N-1) for b in [[True], [False]]]
'''
  L=ciagi_binarne(N-1)
  NL=[]
  for i in L:
    NL.append([True]+i)
    NL.append([False]+i)
  return NL
'''   
#2 -> [ [False, False], [False, True], [True, False], [True, True] ]    

def wartosciowania(zmienne):
  cb = ciagi_binarne(len(zmienne))
  #print([dict(zip(zmienne, ciag)) for ciag in cb])
  return [ dict(zip(zmienne, ciag)) for ciag in cb]
  
def wartosc_formuly(F, wart):
  F = F.replace('*', ' and ')
  F = F.replace('+', ' or ')
  F = F.replace('-', ' not ')
  F = F.replace('T', ' True ')
  F = F.replace('F', ' False ')
  print (F, wart)
  return eval(F, wart)
  
def spelnialna(F):
  zmienne = lepsze_zmienne(F)
  for wart in wartosciowania(zmienne):
    if wartosc_formuly(F, wart) == True:
      return True
  return False    

def tautologia(F):
  zmienne = lepsze_zmienne(F)#set(F) - set('TF+*()- ')
  for wart in wartosciowania(zmienne):
    if wartosc_formuly(F, wart) == False:
      return False
  return True

def lepsze_zmienne(F):
  for i in F:
    if not i.islower():
      F = F.replace(i, ' ')
  F = set(F.split())
  return F
'''
  F = F.replace('*', ' ')
  F = F.replace('+', ' ')
  F = F.replace('-', ' ')
  F = F.replace('T', ' ')
  F = F.replace('F', ' ')
  F = F.replace('(', ' ')
  F = F.replace(')', ' ')
'''
  
# T,F -> stałe
print(tautologia('p+(-p)'))
print (tautologia('F'))
print(spelnialna('p*(-ala)'))
