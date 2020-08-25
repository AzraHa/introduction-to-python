n = int(input())
b = 0
t = 1

while b<n:
    t += 1
    cudan = True
    kopija = t
    while kopija>0:
        if kopija%10!=2 and kopija%10!=3:
            cudan = False
        kopija //=10

    if cudan:
        b +=1
print(t)
