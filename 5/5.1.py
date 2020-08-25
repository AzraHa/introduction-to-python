#Program od korisnika traži unos broja n.
# Nakon toga program predviđa vjerovatnocu dobijanja n uzastopnih šestica ukoliko bacimo kockicu 30 puta.
# Za što tacnije predviđanje potrebno je izvršiti tacno 10000 simulacija.
import random

n = int(input()) #n dobijanja sestica
broj_simulacija = 10000
broj_uspjeha = 0

for i in range(broj_simulacija):
    broj_sestica = 0
    for j in range(30): #30 puta baca kockicu
        kockica = random.randint(1,6) #nasumican broj 1-6
        if kockica == 6:
            broj_sestica += 1
        else:
            broj_sestica = 0
        if broj_sestica >= n:
            broj_uspjeha += 1
            break

print(100* broj_uspjeha / broj_simulacija)

