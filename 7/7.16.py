lista = input()
lista = lista.split()
lista = [int(x) for x in lista]
skupine = 0
uzastopni = False
for i in range(1,len(lista)):
    if lista[i-1] == lista[i] and not uzastopni:
        skupine += 1
        uzastopni = True
    if lista[i-1]!= lista[i]:
        uzastopni = False
print(skupine)
