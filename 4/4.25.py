n = int(input())
broj_finih = 0
broj = 9
while broj_finih != n:
    broj +=1
    t = broj
    c1 = t%10
    t //= 10
    while t>0:
        c2 = t%10
        if c1+c2 == 4:
            broj_finih +=1
            break
        c1 = c2
        t //=10

print(broj)
