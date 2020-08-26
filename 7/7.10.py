n = int(input())
lista = []
for i in range(n):
    red = []
    for i in range(n):
        red.append(int(input()))
    lista.append(red)
s1 = 0
s2 = 0
for j in range(len(lista[0])):
    for k in range(len(lista[0])):
        if j == k:
            s1 += lista[j][k]
        if k+j == len(lista)-1:
            s2 += lista[j][k]
print(s1*s2)
