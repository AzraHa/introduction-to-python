n = input()
H = 0
S = 0
b = 0
while n!="":
    n = float(n)
    if b%2==0:
        H+=n
    else:
        S+=n
    b+=1
    n = input()

print(H-S)
