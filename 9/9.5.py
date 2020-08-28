fajl = open("test01.in","r")
matrica = []
while True:
    s = fajl.readline()
    if s == "":
        break
    matrica.append(s.split())
brojKoraka = 0
x = 0
y = 0
for i in range(len(matrica)):
    for j in range(len(matrica[i])):
        if matrica[i][j] == "R":
            x = i
            y = j
while y < len(matrica[x]) - 1 and matrica[x][y + 1] == "-":
    y += 1
    brojKoraka += 1
if y == len(matrica[x])-1:
    brojKoraka += 1
    print(brojKoraka)
    print("DA")
else:
    while x < len(matrica)-1 and matrica[x + 1][y] == "-":
        x += 1
        brojKoraka += 1
    if x == len(matrica)-1:
        brojKoraka += 1
        print(brojKoraka)
        print("DA")
    else:
        print(brojKoraka)
        print("NE")
