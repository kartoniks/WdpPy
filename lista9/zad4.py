from turtle import *
from math import *

tracer(0,1)
alpha=0
def kwadrat(BOK, kolor='red'):
  pd()
  fillcolor(kolor)
  begin_fill()
  for i in range(4):
    fd(BOK)
    rt(90)
  end_fill() 
  pu()

def p_tree(b, n):
  if n==0:
    return
  kwadrat(b)
  fd(b)
  lt(45)
  p_tree(b/sqrt(2), n-1)
  rt(90)
  fd(b/sqrt(2))
  p_tree(b/sqrt(2), n-1)
  bk(b/sqrt(2))
  lt(45)
  bk(b)
#kwadrat(0,0,100,'red')
pu()
lt(90)
bk(100)
p_tree(100,9)
x=input()
