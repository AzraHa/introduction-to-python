a = int(input())
b = int(input())
for i in range(a,b+1):
    suma = 0
    for j in range(1,i//2+1):
        if i%j == 0:
            suma += j
    if suma == i:
        print(i,end= " ")
