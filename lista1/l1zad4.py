from losowanie_fragmentow import losuj_fragment

def rob_haslo(n):
    haslo=""
    temp=""
    while( len(haslo) < n):
        haslo += losuj_fragment()
        if( len(haslo) == n-2):
            while(len(temp) !=2):
                temp = losuj_fragment()
            haslo += temp
            print(haslo)
            return 0  
        if( len(haslo) == n-3):
            while(len(temp) !=3):
                temp = losuj_fragment()
            haslo += temp
            print(haslo)
            return 0  
        if( len(haslo) == n-4):
            while(len(temp) !=4):
                temp = losuj_fragment()
            haslo += temp
            print(haslo)
            return 0    
        
#for i in range(5):
#    print ( losuj_fragment() )
for i in range(10):
    rob_haslo(8)
for i in range(10):
    rob_haslo(12)


