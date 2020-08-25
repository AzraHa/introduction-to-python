import random
BROJ_SIM = 10000
broj_sudara = 0
for i in range(BROJ_SIM):
    r1x = 0
    r1y = 0
    r2x = 2
    r2y = 0
    sudar = False
    for j in range(10):
        smjer = random.randint(1, 4)
        if smjer == 1:
            r1y += 1
        elif smjer == 2:
            r1y -= 1
        elif smjer == 3:
            r1x -= 1
        elif smjer == 4:
            r1x += 1
        if r1x == r2x and r1y == r2y:
            sudar = True
    smjer = random.randint(1, 4)
    if smjer == 1:
        r2y += 1
    elif smjer == 2:
        r2y -= 1
    elif smjer == 3:
        r2x -= 1
    elif smjer == 4:
        r2x += 1
    if r1x == r2x and r1y == r2y:
        sudar = True
    if sudar:
        broj_sudara += 1
print(broj_sudara / BROJ_SIM)
