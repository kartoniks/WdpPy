from turtle import *
from duze_cyfry import dajCyfre
import random

speed('fastest')

def kwadrat(bok):
  R = 0.5
  G = 0.5
  B = 0.5
  pd()
  fillcolor((R,G,B))
  begin_fill()
  for i in range(4):
    fd(bok)
    rt(90)
  end_fill()
  pu()

def rzad(napis, bok):
  for i in napis:
    if i == '#':
      kwadrat(bok)
    fd(bok)
  fd(bok)
'''
BOK = 30
for j in range(10):
  for i in range(10):
    kwadrat(BOK)
    fd(BOK)
  up()
  bk(10*BOK)
  left(90)
  fd(BOK)
  rt(90)
  down()
'''
def wypisz(n):
  s=str(n)
  L=[[0]*5 for i in range(len(s))]
  for i in range(len(s)):
    L[i] = dajCyfre(int(s[i]))
  for i in range(5):
    for j in range(len(s)):
      rzad(L[j][i],10)
    bk(10*6*len(s))
    rt(90)
    fd(10)
    lt(90)
      #print(L[j][i], end=" ")
    #print("")


x = 1234
wypisz(x)
input()




