lista = []
n = int(input())
for i in range(n):
    lista.append(int(input()))
m = int(input())
lista.sort()
nova_lista = [] + lista[m:len(lista)-m]
print(nova_lista)
