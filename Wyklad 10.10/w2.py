def potega(a,n):
    if(n==0):
        return 1
    return potega(a,n-1)*a

def potega2(a,n):
    wynik = 1
    while(n>0):
        wynik*=a
        n=n-1
    return wynik




for i in range(10):
    print(potega2(2,i))
