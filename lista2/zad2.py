from random import randint

def generuj(n,l):
	for i in range(n):
		l[i]=randint(1,6)

def sprawdz(n,l):
	for i in range(n-5):
		goodl=0
		for j in range(5):
			if(l[j+i]>=l[j+i+1]):
				goodl+=1
		if goodl==5:
			return 1
		#print(i, goodl)
	return 0


l=[0]*100

generuj(100,l)
#print(l)
#print(sprawdz(100,l))


dobre=0
for i in range(100):
	generuj(100,l)
	if sprawdz(100,l):
		dobre+=1
print(dobre/100)

