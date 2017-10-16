def rev1(L):
    L0 = L[:]    #kopiowanie listy
    for i in range(len(L0) // 2):
        j = len(L0)-1-i
        L0[i], L0[j] = L0[j], L0[i]
    return L0

def rev2(L):
    wynik = []
    for i in range(len(L)):
        wynik.append(L[len(L)-1-i])
    return wynik

def rev3(L):
    wynik = []
    for e in L:
        wynik = [e] + wynik
    return wynik
#L[1:3] - odwolanie do elementów listy od 2 do 3
def rev4(L):
    if len(L) == 0:
        return []
    return rev4(L[1:]) + [L[0]]
L = [1,2,3,4,'hej']

print(rev1(L))
print(rev2(L))
print(rev3(L))
print(rev4(L))
