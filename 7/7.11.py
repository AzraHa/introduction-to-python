n = int(input())
lista = []
for i in range(n):
    red = []
    for j in range(n):
        red.append(int(input()))
    lista.append(red)
for i in range(n):
    suma = 0
    for j in range(n):
        suma += lista[j][i]
    print(suma)
