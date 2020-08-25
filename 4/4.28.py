r = int(input())
k = int(input())
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
for i in range(r):
    for j in range(k):
        if i>=y1 and i<=y2 and j>=x1 and j<=x2:
            print("x",end = " ")
        else:
            print("-",end=" ")
    print()
