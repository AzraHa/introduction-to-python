n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
nova_lista = []+ lista
nova_lista.sort()
srednja = nova_lista[n//2]
lista.remove(srednja)
for element in lista:
    print(element,end = " ")
