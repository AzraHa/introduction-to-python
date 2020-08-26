m = int(input())
lista = []
for i in range(m):
    lista.append(int(input()))
pivot = lista[m//2]
lijeva = []
desna = []
for i in range(len(lista)):
    if lista[i]<pivot:
        lijeva.append(lista[i])
    elif lista[i]>pivot:
        desna.append(lista[i])
nova_lista = [] + lijeva + desna
nova_lista.insert(len(lijeva),pivot)
print(nova_lista)
