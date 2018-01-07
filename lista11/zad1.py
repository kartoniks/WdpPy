def caesar(s,k):
  alfa = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
  number = [i for i in range(len(alfa))]
  dic ={}
  for i in range(len(alfa)):
    dic[alfa[i]]=number[i]
    dic[number[i]]=alfa[i]
  #print(dic)
  res=[dic[(dic[l] + k) % len(alfa)] for l in s]
  return ''.join(res)

#print(ceasar("żabamała",1))

for i in range(10):
  print(caesar(caesar("arturiżółw", i),-i))
