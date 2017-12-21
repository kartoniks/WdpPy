def solve(word):
  letters = set()
  word = word.split()
  for i in word:
    for j in i:
      letters.add(j)  
  letters = list(letters) #tworzenie listy liter  
  #print(letters, digits)
  return backtrack(word, letters)

def backtrack(w, l):
  print(w,l)
  if len(l) == 0:
    if check(w):  
      return w
    else:
      return None
  else:  
    myc = l.pop()
    for i in range(10):
      if(str(i) in w[0] or str(i) in w[1] or str(i) in w[2]):
        continue
      for x in range(3):
        w[x] = w[x].replace(myc, str(i))
      #print(w, l, myc, str(i))
      return backtrack(w,l)

def check(w):
  return (int(w[0])+int(w[1]) ) == int(w[2])

print(solve("send more money") )

