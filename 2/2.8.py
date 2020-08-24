import math

a = float(input())
b = float(input())
c = float(input())
O = math.radians(float(input()))
F = math.radians(float(input()))

x = a * math.sin(O) * math.cos(F)
y = b * math.cos(O) * math.sin(F)
z = c * math.sin(O)

print(x,y,z,end="\n")
