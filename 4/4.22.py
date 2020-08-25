n = int(input())
for i in range (n):
    for j in range(n*2+1):
        if i%2 == 0:
            print("x",end="")
        else:
            if (i+j)%2 == 0:
                print("0",end="")
            else:
                print("x",end="")
    print()

