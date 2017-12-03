def ukladalne(s, w):
  ds = slownikuj(s)
  dw = slownikuj(w)
  for i in ds:
    if i not in dw:
      return False
    if dw[i]<ds[i]:
      return False
  return True

def slownikuj(s):
  d = {}
  for i in s:
    if i not in d:
      d[i] = 0
    d[i] += 1
  return d


print(ukladalne("kot", "lokomotywa"))
print(ukladalne("kotka", "lokomotywa"))
