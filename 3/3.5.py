from math import sqrt
epsilon = 0.0000000001

Ax = float(input())
Ay = float(input())

Bx = float(input())
By = float(input())

r = float(input())
d = sqrt((Bx-Ax)**2 + (By-By)**2)
dr = r * 1.5

if d<dr:
    print("Kruznice se sijeku")
elif d-dr<epsilon and dr-d<epsilon:
    print("kruznice se dodiruju")
else:
    print("kruznice nemaju zajednickih tacaka")
