from random import randint

def kostka():
    return randint(1,6)


licznik = 0

while True:
    k1=kostka()
    k2=kostka()
    licznik+=1
    print(licznik,k1,k2)
    if k1+k2 == 12:
        break
