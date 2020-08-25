import random
random.seed(42)
broj_simulacija = 10000
cilj = 0
for i in range(broj_simulacija):
    x = 0
    y = 0
    for j in range(10):
        korak = random.randint(1,4)
        if korak == 1:
            y +=1
        elif korak == 2:
            y -=1
        elif korak == 3:
            x -=1
        elif korak == 4:
            x += 1
    if x == 0 and y == 0:
        cilj +=1

print(cilj/broj_simulacija)

