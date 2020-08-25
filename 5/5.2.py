#Nedim ima standardnu kockicu sa 6 strana numerisanu brojevima od 1 do 6,
# a Amina ima kockicukoja ima 9 strana numerisanih brojevima od 1 do 9.
#Obje kockice su fer, što znaci da vjerovatnoća dobivanja jedne od stranica je jednaka za sve stranice.
# Nedim baca svoju kockicu, a potom i Amina.Koja je vjerovatnoca da ćw Nedim dobiti broj
# koji je veći od broja na Amininoj kockici.
# Da biste došli do odgovora potrebno je simulirati 10000 partija bacanja kockica.

import random
broj_simulacija = 10000
broj_uspjeha = 0
for i in range(broj_simulacija):
    if random.randint(1,6) > random.randint(1,9):
        broj_uspjeha +=1

print(broj_uspjeha/broj_simulacija)
