import random
dolazi = int(input())
opklada = int(input())
osvojiti = int(input())
broj_pobjeda = 0
broj_simulacija = 10000
for i in range(broj_simulacija):
    novac = dolazi
    while novac > 0 and novac < osvojiti:
        if random.randrange(0,100) < 49:
            novac += opklada
        else:
            novac -= opklada
    if novac>= osvojiti:
        broj_pobjeda +=1

print(broj_pobjeda/broj_simulacija)
