import math

x = float(input())
y = float(input())

r = math.sqrt(x*x+y*y)

fi = math.atan2(y,x)

print(r,math.degrees(fi),end="\n")
