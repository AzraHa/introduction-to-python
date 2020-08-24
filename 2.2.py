import math
x = float(input())
y = float(input())
L = float(input())
g = 9.81
brojnik = x*x*g
Lrad = math.radians(L)
nazivnik = x*math.sin(2*Lrad)- 2*y*math.cos(Lrad)*math.cos(Lrad)

print(math.sqrt(brojnik/nazivnik))
