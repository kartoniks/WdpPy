
alfa = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
number = [i for i in range(32)]
dic ={}
slowa={}
wynik=[]

for i in range(len(alfa)):
  dic[alfa[i]]=number[i]
  dic[number[i]]=alfa[i]

def caesar(s,k, slownik = dic):
  #print(dic)
  res=[slownik[(slownik[l] + k) % 32] for l in s]
  return ''.join(res)

def jestpara(s, slownik=slowa):
  for i in range(1,32):
    if caesar(s,i) in slownik:
      return (s, caesar(s,i), i)
  return False

def literowe(slowo, a=alfa):
  for l in slowo:
    if l not in a:
      return False
  return True

for w in open('slowa.txt'):
  w=w.strip()
  w=w.lower()
  if literowe(w):
    if len(w) in slowa:
      slowa[len(w)][w]=True
    else:
      slowa[len(w)]={}

#print(slowa.keys())


for l in range(8,3,-1):
  print(l)
  if l in slowa.keys():
    for w in slowa[l]:
      if jestpara(w, slowa[l]):
        wynik.append( jestpara(w,slowa[l]))
    if not wynik == []:
      break

print(wynik)

