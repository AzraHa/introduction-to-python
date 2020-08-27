tekst = input()
rijeci = tekst.lower().split()
ciste_rijeci = []
max = 0
for r in rijeci:
    rijec = r.strip(",.-?! ")
    ciste_rijeci.append(rijec)
    if len(rijec) > max:
        max = len(rijec)
for r in ciste_rijeci:
    if len(r) == max:
        print(r)
