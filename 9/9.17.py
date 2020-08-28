fajl = open("test01.in","r")
klubovi = dict()
for red in fajl:
    red = red.strip().split()
    if red[0] not in klubovi:
        klubovi[red[0]] = 0
    if red[4] not in klubovi:
        klubovi[red[4]] = 0
    if int(red[1])>int(red[3]):
        klubovi[red[0]] += 3
    elif int(red[1])< int(red[3]):
        klubovi[red[4]] += 3
    else:
        klubovi[red[0]] += 1
        klubovi[red[4]] += 1

v = list(klubovi.values())
k = list(klubovi.keys())

for i in range(len(klubovi)):
    for j in range(len(klubovi)-1):
        if(v[j]<v[j+1]):
            temp = v[j]
            v[j] = v[j+1]
            temp = k[j]
            k[j] = k[j+1]
            k[j+1] = temp

for i in range(len(klubovi)):
    print(k[i],v[i])
