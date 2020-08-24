n = int(input())
for i in range(n):
    a = int(input())
    for j in range(a):
        if(i%2==0):
            print(n*"-",end="")
        else:
            print(n*"*",end="")
    print()

