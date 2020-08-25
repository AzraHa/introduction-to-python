import random
BROJ_SIMULACIJA = 100000
broj_boja = 0
for i in range(BROJ_SIMULACIJA):
    crvena = False
    zelena = False
    plava = False
    granica_crvene = 5
    granica_zelene = 10
    kuglica1 = random.randrange(15)
    if kuglica1 < granica_crvene:
        crvena = True
        granica_crvene -= 1
        granica_zelene -= 1
    elif kuglica1 < granica_zelene:
        zelena = True
        granica_zelene -= 1
    else:
        plava = True
    kuglica2 = random.randrange(14)
    if kuglica2 < granica_crvene:
        crvena = True
        granica_crvene -= 1
        granica_zelene -= 1
    elif kuglica2 < granica_zelene:
        zelena = True
        granica_zelene -= 1
    else:
        plava = True
    kuglica3 = random.randrange(13)
    if kuglica3 < granica_crvene:
        crvena = True
        granica_crvene -= 1
        granica_zelene -= 1
    elif kuglica3 < granica_zelene:
        zelena = True
        granica_zelene -= 1
    else:
        plava = True
    kuglica4 = random.randrange(12)
    if kuglica4 < granica_crvene:
        crvena = True
        granica_crvene -= 1
        granica_zelene -= 1
    elif kuglica4 < granica_zelene:
        zelena = True
        granica_zelene -= 1
    else:
        plava = True
    if plava == True:
        broj_boja += 1
    if zelena == True:
        broj_boja += 1
    if crvena == True:
        broj_boja += 1
print(broj_boja/BROJ_SIMULACIJA)
