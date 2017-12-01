S=set()
dobre=set()
for i in open('slowa.txt'):
  i=i.strip()
  S.add(i)

for i in S:
  if i[::-1] in S and i not in dobre:
    print(i, i[::-1])
    dobre.add(i[::-1])

#for i in dobre:
#  print(i, i[::-1])
