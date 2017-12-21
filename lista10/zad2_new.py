def solve(word):
  letters = {}
  word = word.split()
  for i in word:
    for j in i:
      letters[j] = -1
  print(letters)
  return backtrack(word, letters)

def backtrack(w, l):
  if -1 not in l.keys():
    if (eval(w[0], l)+eval(w[1],l) == eval(w[2],l) ):
      return l
    else:
      return None
  for i in w:
    for j in i:
      if l[j] != -1:
        for x in range(10):
          if x not in l.keys():
            l[j] = x
            return backtrack(w,l)
            


def check(w):
  return (int(w[0])+int(w[1]) ) == int(w[2])

print(solve("send more money") )

