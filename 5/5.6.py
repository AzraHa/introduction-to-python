import random
broj_simulacija = 10000
broj_uspjeha = 0

for i in range(broj_simulacija):
    ppn = 0
    pn = 0
    for j in range(10):
        nota = random.randint(1,7)
        if ppn == 1 and pn == 3 and nota == 5:
            broj_uspjeha +=1
            break
        ppn = pn
        pn = nota
print(broj_uspjeha/broj_simulacija)
