from math import sqrt
x = float(input())
y = float(input())
r = float(input())

Ax = float(input())
Ay = float(input())

epsilon = 0.0000000001
d = sqrt((Ax-x)**2 + (Ay-y)**2)

if d<r:
    print("Tacka pripada unutrasnjosti kruga")
elif r-d < epsilon and d-r<epsilon:
    print("Tacka pripada kruznici")
else:
    print("Tacka ne pripada krugu")
