matrica = []
smjer = ""
l_red = 0
l_kol = 0
redova = 0
kolona = 0
with open("test01.in","r") as f:
    br_red = 0
    for red in f:
        red = red.strip().split()
        if red[0] == "*" or red[0] == "-":
            matrica.append(red)
        else:
            smjer = red[0]
        if "*" in red:
            l_red = br_red
            l_kol = red.index("*")
        br_red += 1
    redova = len(matrica)
    kolona = len(matrica[0])

for i in range(100):
    if smjer == "SI":
        if l_red-1 >= 0 and l_kol+1 < kolona:
            l_red = l_red-1
            l_kol = l_kol+1
        elif l_red-1 < 0 and l_kol+1 >= kolona:
            l_red = l_red+1
            l_kol = l_kol-1
            smjer = "JZ"
        elif l_red-1 < 0 and l_kol+1 < kolona:
            l_red = l_red+1
            l_kol = l_kol+1
            smjer = "JI"
        elif l_red-1 >= 0 and l_kol+1 >= kolona:
            l_red = l_red-1
            l_kol = l_kol-1
            smjer = "SZ"
    elif smjer == "SZ":
        if l_red-1 >= 0 and l_kol-1 >= 0:
            l_red = l_red-1
            l_kol = l_kol-1
        elif l_red-1 < 0 and l_kol-1 < 0:
            l_red = l_red+1
            l_kol = l_kol+1
            smjer = "JI"
        elif l_red-1 < 0 and l_kol-1 >= 0:
            l_red = l_red+1
            l_kol = l_kol-1
            smjer = "JZ"
        elif l_red-1 >= 0 and l_kol-1 < 0:
            l_red = l_red-1
            l_kol = l_kol+1
            smjer = "SI"
    elif smjer == "JI":
        if l_red+1 < redova and l_kol+1 < kolona:
            l_red = l_red+1
            l_kol = l_kol+1
        elif l_red+1 >= redova and l_kol+1 >= kolona:
            l_red = l_red-1
            l_kol = l_kol-1
            smjer = "SZ"
        elif l_red+1 >= redova and l_kol+1 < kolona:
            l_red = l_red-1
            l_kol = l_kol+1
            smjer = "SI"
        elif l_red+1 < redova and l_kol+1 >= kolona:
            l_red = l_red+1
            l_kol = l_kol-1
            smjer = "JZ"
    elif smjer == "JZ":
        if l_red+1 < redova and l_kol-1 >= 0:
            l_red = l_red+1
            l_kol = l_kol-1
        elif l_red+1 >= redova and l_kol-1 < 0:
            l_red = l_red-1
            l_kol = l_kol+1
            smjer = "SI"
        elif l_red+1 < redova and l_kol-1 < 0:
            l_red = l_red+1
            l_kol = l_kol+1
            smjer = "JI"
        elif l_red+1 >= redova and l_kol-1 >= 0:
            l_red = l_red-1
            l_kol = l_kol-1
            smjer = "SZ"
    matrica[l_red][l_kol] = "*"
for red in matrica:
    print(*red,sep=" ")



