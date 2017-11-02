from duze_cyfry import dajCyfre

def wypisz(n):
    s=str(n)
    L=[[0]*5 for i in range(len(s))]
    for i in range(len(s)):
        L[i] = dajCyfre(int(s[i]))
    for i in range(5):
        for j in range(len(s)):
            print(L[j][i], end=" ")
        print("")

x = input()
wypisz(x)
