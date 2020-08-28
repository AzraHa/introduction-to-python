import  collections
with open("test01.in") as f:
    redovi = list(f)
d = collections.OrderedDict()
for red in redovi:
    elementi = red.strip().split(maxsplit=2)
    kljuc = elementi[0] + " " + elementi[2]
    vrijednost = elementi[1]
    adrese = d.get(kljuc,set())
    adrese.add(vrijednost)
    d[kljuc] = adrese
ispisane = set()
for k,v in d.items():
    if len(v) > 4:
        adresa = k.split()[0]
        if adresa not in ispisane:
            print(adresa)
            ispisane.add(adresa)

