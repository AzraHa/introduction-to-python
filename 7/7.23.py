brojevi = input()
brojevi = brojevi.split()
lista = [int(x) for x in brojevi]

najvecaS = 0

for i in range(len(lista)):
    suma = 0
    for j in range(i,len(lista)):
        suma += lista[j]
        if najvecaS < suma:
            najvecaS = suma

print(najvecaS)
