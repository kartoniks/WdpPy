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

print(permutacyjna('indianin'))
