import math
b = float(input())
c = float(input())
L = math.radians(float(input()))
a = b*b + c*c - 2*b*c*math.cos(L)
print(math.sqrt(a))
