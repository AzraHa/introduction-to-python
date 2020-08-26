lista = input()
lista = lista.split()
lista  = [int(x) for x in lista]
n = int(input())
lista.sort(reverse=True)
print(lista[0] - lista[n-1])
