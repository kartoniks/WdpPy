def reprezentant(L):
  maks=0
  for i in L:
    if i>maks:
      maks = i
  cand=maks
  for i in L:
    if len(str(i)) == len(str(maks)) and i<maks:
      cand = i
  return(cand)



reprezentant([1,2,3,44,55])
