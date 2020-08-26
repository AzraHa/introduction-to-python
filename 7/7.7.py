n = input()
lista = []
while n!="":
    lista.append(n)
    n = input()
prosjek = 0
for i in range(len(lista)):
    prosjek += len(lista[i])
prosjek = prosjek / len(lista)

for i in range(len(lista)):
    if len(lista[i])>prosjek:
        print(lista[i], end = "\n")
