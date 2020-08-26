fajl = open("test01.in","r")
drzave = dict()
for red in fajl:
    podaci = red.strip().split(", ")
    if podaci[1] not in drzave or \
        drzave[podaci[1]][1] < int(podaci[2]):
    drzave[podaci[1]] = [podaci[0], int(podaci[2])]
gradovi = []
for kljuc, lista in drzave.items():
    gradovi.append(lista[0])
gradovi.sort()
for grad in gradovi:
print(grad)
