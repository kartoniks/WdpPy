def draw(n):
    for i in range(n):
        print(" "*n, "*"*n, " "*n, sep="")
    for i in range(n):
        print("*"*3*n, sep="")
    for i in range(n):
        print(" "*n, "*"*n, " "*n, sep="")



draw(4)
