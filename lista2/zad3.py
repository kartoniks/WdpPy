def kolko(s,r):
    for i in range(2*r):
        print(s*" ", end="")
        for j in range(2*r):
            if((i+0.5-r)*(i+0.5-r)+(j+0.5-r)*(j+0.5-r)<=r*r):
                print("*", end="")
            else:
                print(" ", end="")
        print("")





kolko(5,5)
kolko(3,7)
kolko(1,9)


