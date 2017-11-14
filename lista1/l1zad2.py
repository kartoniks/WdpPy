from math import log

def silnia(n):
    wynik = 1
    for i in range(1,n+1):
        wynik*=i
        s.append(wynik)

def writeout(n):
    for i in range(3,n):
        temp = log(s[i])/log(10)+1
        temp = int(temp)
        
        print(i+1, "! ma ", temp, " cyfr", sep='', end="")
        if(( (temp // 10) != 1) and (2 <= temp%10 <= 4)):
            print("y", end="")
        print("")

s = list()
silnia(100)
writeout(100)


    
