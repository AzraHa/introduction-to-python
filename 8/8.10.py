n = int(input())
lista = []
for i in range(n):
    lista.append(input())
duzina = 0
for element in lista:
    if len(element) > duzina:
        print(element)
    duzina += len(element)
