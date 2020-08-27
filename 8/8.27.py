recenica = input().lower().split()
for i in range(len(recenica)):
    recenica[i] = recenica[i].strip(" .,!?:;")
provjerene = set()
ponavljanja = []
for rijec in recenica:
    broj_ponavljanja = 0
    if rijec not in provjerene:
        broj_ponavljanja = recenica.count(rijec)
        provjerene.add(rijec)
    if broj_ponavljanja>1:
        ponavljanja.append([rijec,broj_ponavljanja])
for element in ponavljanja:
    print(element[0],": ",element[1],sep = "")

