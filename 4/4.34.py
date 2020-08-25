r = int(input())
k = int(input())
x1 = int(input())
y1 = int(input())
d = int(input())

for i in range(r):
    for j in range(k):
        if i < y1 or i > y1 + d - 1 or j < x1 or j > x1 + d -1 or j < x1 + (i - y1):
            print("-",end =" ")
        else:
            print("X",end=" ")
    print()

