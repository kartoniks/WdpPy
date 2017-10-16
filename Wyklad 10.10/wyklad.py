import math

D = 40

for i in range(100):
    ile_gwiazdek = int(abs(math.sin(i/10))*D)
    print( (D-ile_gwiazdek)*' ' + ile_gwiazdek * '*')
    
