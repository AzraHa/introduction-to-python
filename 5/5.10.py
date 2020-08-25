import random
BROJ_SIMULACIJA = 10000
preskocio = 0
mapa = input()
minmax = [int(x) for x in input().split()]
z1 = mapa.index("!")
z2 = mapa.index("!", z1+1)
kraj = len(mapa)
for i in range(BROJ_SIMULACIJA):
    poz = mapa.index("*")
    while poz <= z1:
        poz += random.randint(minmax[0], minmax[1])
    if poz >= z2:
        preskocio += 1
print(preskocio/BROJ_SIMULACIJA)
