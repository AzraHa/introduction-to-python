import math
def pozicija(p,s,k):
    if s=="G" :
        p[1] += k
    elif s=="DO":
        p[1] -= k
    elif s == "DE":
        p[0] += k
    elif s== "L":
        p[0] -= k
    return p
fajl = open("test01.in","r")
pozicije = dict()
for red in fajl:
    r,s,k = red.strip().split()
    k = int(k)
    if r not in pozicije:
        pozicije[r] = pozicija([0,0],s,k)
    else:
        pozicije[r] = pozicija(pozicije[r],s,k)

for k in sorted(pozicije.keys()):
    print(k,end = " ")
    print(math.sqrt(pow(pozicije[k][0],2) + pow(pozicije[k][1],2)))
