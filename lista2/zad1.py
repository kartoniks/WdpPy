def rysuj(n,k):
    for i in range(2*n):
        for j in range(k):
            for l in range(n):
                if(i%2==0):
                    print(k*' ', k*'*', sep = "", end = "")
                else:
                    print(k*'*', k*' ', sep = "", end = "")
            print("")        
	
rysuj(4,5)
