n = int(input())
m = int(input())

for i in range(1,n+1):
    if i<10:
        print(" ",end = "")
        print(i,end = " ")
    else:
        print(i,end =" ")
    if i%m == 0:
        print()
