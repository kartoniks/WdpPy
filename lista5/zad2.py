from turtle import *

speed('fastest')

def rtree(dlug,it,kat):
  if it == 0:
    return 0
  fd(dlug)
  lt(kat)
  rtree(dlug*0.8, it-1, kat)
  rt(2*kat)
  rtree(dlug*0.8, it-1, kat)
  lt(kat)
  bk(dlug)


lt(90)
rtree(50,7,30)
input()
