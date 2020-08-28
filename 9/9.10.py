fajl = open("test01.in","r")
red = fajl.readline().split()
redovi = int(red[0])
kolone = int(red[1])
matrica = []
for i in range(redovi):
    red = []
    for j in range(kolone):
        red.append(" ")
    matrica.append(red)

linija = fajl.readline()
while linija!="":
    (red,kolona,znak) = linija.split()
    red = int(red.strip("(,"))
    kolona = int(kolona.strip(")"))
    matrica[red][kolona] = znak
    linija = fajl.readline()
for i in range(redovi):
    for j in range(kolone):
        print(matrica[i][j], end = " ")
    print()
