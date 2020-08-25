import random

def kraljica_napada(y,x):
    for i in range(8):
        if i!=x and p[y][i] != "-":
            return True
        if i!=y and p[i][x] != "-":
            return True

    return False

broj_simulacija = 10000
broj_napadanja = 0
for i in range(broj_simulacija):
    p =[]
    for i in range(8):
        p.append(["-"]*8)
        broj_kraljica = 0
    while broj_kraljica < 3:
        x = random.randrange(8)
        y = random.randrange(8)
        if p[y][x] == "-":
            p[y][x] = "*"
            broj_kraljica +=1
    napadaju_se = False
    for i in range(8):
        for j in range(8):
            if p[i][j] == "*" and kraljica_napada(i,j):
                napadaju_se = True
    if napadaju_se:
        broj_napadanja +=1

print(broj_napadanja/broj_simulacija)
