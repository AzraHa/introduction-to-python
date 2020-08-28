mapa = {"A" : 0, "B" : 1, "C" : 2, "D": 3, "E" : 4}
svi_odgovori = []
fajl = open("test01.in","r")
sb, pb = fajl.readline().split()
sb = int(sb) # broj studenata
pb = int(pb) # broj pitanja
for i in range(sb*pb):
    odgovori_pitanje = fajl.readline().split()
    odgovori_pitanje = [int(x)<=127 for x in odgovori_pitanje]
    svi_odgovori.append(odgovori_pitanje)

tacni = fajl.readline().split()
fajl.close()

rezultati = []
for i in range(sb):
    broj_tacnih = 0
    for j in range(pb):
        pitanje= svi_odgovori[i*pb+j]
        if pitanje.count(True) == 1 and pitanje[mapa[tacni[j]]] == True:
            broj_tacnih +=1
    rezultati.append(broj_tacnih)

for element in rezultati:
    print(element)
