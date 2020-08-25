#Napisati program koji dozvoljava unos dužine stranice kvadrata, koja je tipa float.
# Program potom racuna ocekivanu (tj. prosjecnu) udaljenost izmedu dvije nasumicno odabrane take unutar kvadrata.
import random
import math
stranica = float(input())
broj_simulacija = 10000
ukupno = 0
for i in range(broj_simulacija):
    x1 = random.uniform(0,stranica)
    y1 = random.uniform(0,stranica)
    x2 = random.uniform(0,stranica)
    y2 = random.uniform(0,stranica)

    d = math.sqrt((x2-x1)**2 +(y2-y1)**2)

    ukupno +=d

print(ukupno/broj_simulacija)

