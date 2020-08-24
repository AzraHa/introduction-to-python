import math
v0 = float(input())
R = float(input())
L = float(input())
L = math.radians(L)

g = (v0*v0*math.sin(2*L))/R

print(g)
