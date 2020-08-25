a = int(input())
b = int(input())

temp = b
desetine = 1
bc2 = 0
while temp!=0:
    desetine *=10
    temp //=10
    bc2 +=1

bc1 =0
index = -1
while a!=0:
    temp = a % desetine
    if temp == b:
        index = bc1
    a //= 10
    bc1 += 1

if index == -1:
    print(index)
else:
    print(bc1-index-bc2)

