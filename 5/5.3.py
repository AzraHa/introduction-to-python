#Napisati program koji simulira bacanje dvije kockice. Kockice imaju šest strana i na njima se
#nalaze brojevi od 1 do 6. Program treba izracunati, koliko je prosjecno potrebno bacanja, kako bi
#se tri puta za redom dobio broj veci od 6.
import random
broj_simulacija = 10000
broj_bacanja = 0
for i in range(broj_simulacija):
    b1 = False
    b2 = False
    b3 = False
    broj = 0
    while b1 == False or b2 == False or b3 == False:
        k1 = random.randint(1,6)
        k2 = random.randint(1,6)
        k = k1 + k2
        broj +=1
        b1 = b2
        b2 = b3
        if k>6:
            b3 = True
        else:
            b3 = False
    broj_bacanja += broj
print(broj_bacanja/broj_simulacija)


