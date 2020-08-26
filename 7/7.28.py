def fib_lista():
    lista = []
    lista.append(1)
    lista.append(2)
    for i in range(2,50):
        lista.append(lista[i - 1] + lista[i - 2])
    return lista
fl = fib_lista()
tekst = input()
brojevi = input().split()
brojevi = [int(i) for i in brojevi]
broj_znakova = fl.index(max(brojevi)) + 1
rjesenje = [" "] * broj_znakova
i = 0
for znak in tekst:
    if znak.isalpha():
        rjesenje[fl.index(brojevi[i])] = znak
        i += 1
print("".join(rjesenje).upper())
