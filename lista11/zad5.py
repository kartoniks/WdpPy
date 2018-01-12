alfa = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
def permutacyjna(s):
  dic = {}
  ostatnia = 1
  wynik=[]
  for l in s:
    if l not in dic:
      dic[l] = ostatnia
      ostatnia += 1
    wynik.append(str(dic[l]))
    wynik.append('-')
  return ''.join(wynik[:-1])


slowa = {};
wynik = ''
for s in open('../lista9/slowa.txt'):
  s=s.strip()         
  slowa[permutacyjna(s)] = s  

tekst = 'uwuąpwuw uw dwnuąźhąuąa .'
tekst = tekst.split(' ')
for s in tekst:
  if len(s)>1:
    wynik = wynik + slowa[permutacyjna(s)] + ' '
  else:
    wynik = wynik + s + ' '
print(wynik)



      
