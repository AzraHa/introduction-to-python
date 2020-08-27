rijeci = [input().upper()]
duzina = len(rijeci[0])
for i in range(1,duzina):
    rijeci.append(input().upper())

ispravan = True

for i in range(0,duzina):
    for j in range(0,duzina):
        print(rijeci[i][j],end = " ")
        if(rijeci[i][j]!=rijeci[j][i]):
            ispravan = False
    print()
print("Ispravan" if ispravan else "Neispravan")
