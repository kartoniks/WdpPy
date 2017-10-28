from turtle import *
import random

speed('fastest')

def kwadrat(bok, kolor):
  fillcolor(kolor)
  begin_fill()
  for i in range(4):
    fd(bok)
    rt(90)
  end_fill()

BOK = 30

for j in range(10):
  for i in range(10):
    R = random.random()
    G = random.random()
    B = random.random()
    
    kwadrat(BOK, (R,G,B))
    fd(BOK)
  up()
  bk(10*BOK)
  left(90)
  fd(BOK)
  rt(90)
  down()

input() 
