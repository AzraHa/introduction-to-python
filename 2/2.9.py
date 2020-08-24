import math
alfa = float(input())
beta = float(input())
c = float(input())
gama = 180 - alfa - beta
ar = math.radians(alfa)
br = math.radians(beta)
gr = math.radians(gama)
print(c * (math.sin(ar/2) * math.sin(br/2))/(math.cos(gr/2)))
