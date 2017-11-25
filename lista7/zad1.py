from turtle import *
from duze_cyfry import dajCyfre
from random import *

tracer(0,1)

def kwadrat(bok, kolor):
  if kolor == 0:
    fillcolor("white")
  if kolor == 1:
    fillcolor("red")
  if kolor == 2:
    fillcolor("blue")
  if kolor == 3:
    fillcolor("black")
  if kolor == 4:
    fillcolor("green")
  pd()
  
  begin_fill()
  for i in range(4):
    fd(bok)
    rt(90)
  end_fill()
  pu()

def rysuj(plansza):
  for i in range(h):
    for j in range(w):
      kwadrat(pixsize,plansza[i][j])
      fd(pixsize)
    goto(0,-pixsize*(i+1))

def dodaj(ypoz, xpoz, c,kolor):
  for i in range(5):
    for j in range(5):
      if c[i][j]=='#':
        Board[i+ypoz][j+xpoz]=kolor

def czywolne(ypoz, xpoz, c, kolor):
  for i in range(5):
    for j in range(5):
      if c[i][j]=='#':
        if Board[i+ypoz][j+xpoz] != 0:
          return False
        if Board[(i+ypoz)%h][(j+xpoz-1)%w] == kolor:
          return False
        if Board[(i+ypoz)%h][(j+xpoz+1)%w] == kolor:
          return False
        if Board[(i+ypoz-1)%h][(j+xpoz)%w] == kolor:
          return False
        if Board[(i+ypoz+1)%h][(j+xpoz)%w] == kolor:
          return False
  return True      

pixsize=12
w=25
h=25
Board=[[0 for x in range(w)] for y in range(h)]


dodaj(0, 0, dajCyfre(1), 1)
print(czywolne(0,3, dajCyfre(1), 1))
for i in range(1000):
  k=randint(1,4)
  nowy=randint(0,h-5)
  nowx=randint(0,w-5)
  cyfra=randint(0,9)
  if czywolne(nowy, nowx, dajCyfre(cyfra), k):
    dodaj(nowy, nowx, dajCyfre(cyfra), k)

for i in range(h):
  print(Board[i])
rysuj(Board)
input()

