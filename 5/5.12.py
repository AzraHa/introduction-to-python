import random
n = int(input())
sekvenca = [3, 1, 4, 1]
random.seed(42)
BROJ_SIM = 10000
pobjede = 0
for i in range(BROJ_SIM):
    lista = []
    nalaze_se = True
    for j in range(n):
        lista.append(random.randint(1, 6))
    for broj in sekvenca:
        if broj in lista:
            lista = lista[lista.index(broj)+1:]
        else:
            nalaze_se = False
    if nalaze_se:
        pobjede +=1
print(pobjede/BROJ_SIM)
