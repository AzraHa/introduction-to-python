from math import pi
form math import cos
V = float(input())
O = float(input())
L = float(input())
t = float(input())
o = O * (math.pi/180)
A = 2*V*math.cos(o)
B = 1/t
print(1/((A/L)+B))
