S=set()
dobre=set()
for i in open('slowa.txt'):
  i=i.strip()
  S.add(i)

for i in open('slowa.txt'):
  i=i.strip()
  if i[::-1] in S:
    dobre.add(i)

for i in dobre:
  print(i, i[::-1])
