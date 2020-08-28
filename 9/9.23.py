import math
def provjeri_kvadrat(broj):
    if broj<1:
        return -1
    int_korijen = int(math.sqrt(broj) + 0.5)
    if int_korijen ** 2 == broj:
        return int_korijen
    else:
        return -1
def desifruj(rijec):
    n = provjeri_kvadrat(len(rijec))
    if n == -1 :
        return "GRESKA"

    brojac = 0
    matrica = []
    for i in range(n):
        red = []
        for j in range(n):
            red.append(rijec[brojac])
            brojac += 1
        matrica.append(red)

    rjesenje= ""
    for i in range(n):
        for j in range(n):
            rjesenje += matrica[j][i]
    return  rjesenje

fajl = open("test01.in","r")
for red in fajl:
    red = red.strip()
    print(desifruj(red))
