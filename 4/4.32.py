a = int(input())
b = int(input())
r = max(a,b)
k = abs(a-b)+1

for i in range(r):
    for j in range(k):
        if b<=a and j< i+1 or a<b and j+a> r-i-1:
            print("*",end =" ")
        else:
            print(" ",end=" ")
    print()
