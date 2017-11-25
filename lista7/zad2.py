from turtle import *

def kwadrat(bok,kolor):
  pd()
  fillcolor(kolor)
  begin_fill()
  for i in range(4):
    fd(bok)
    rt(90)
  end_fill()
  pu()




tracer(0,1)
pixlength=6
q=0
for x in open('obraz.txt'):
  q+=pixlength
  L=x.split()
  for i in L:
    k=eval(i)
    myc=(float(k[0])/256, float(k[1])/256, float(k[2])/256)
    print(myc)
    kwadrat(pixlength,myc)
    fd(pixlength)
  goto(0,q)
    
input()
