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
pu()
wypisz(x)
input()




