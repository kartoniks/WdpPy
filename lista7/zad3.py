
bestl=0
bestw=[]

def removesign(words):
  nwords=[]
  for thisw in words:
    be=0
    en=len(thisw)-1
    while( not( 'a'<=thisw[be]<='z') and be<en):
      be+=1
    while( not( 'a'<=thisw[en]<='z') and be<en):
      en-=1
    nwords.append(thisw[be:en+1])
  return nwords

def addlongest(words):
  global bestl
  global bestw
  for w in words:
    if len(w) > bestl:
      bestw = [w]
      bestl = len(w)
    elif len(w) == bestl:
      bestw.append(w)



for x in open('lalka.txt'):
  words=x.split()
  words=removesign(words)
  addlongest(words)

print(bestw)
    
  

