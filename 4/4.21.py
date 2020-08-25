n = int(input())
opadajuce = False
trenutna = 0
while n!=0:
    trenutna = n%10
    if trenutna <= (n//10)%10:
        n= n//10
        opadajuce = True
    n = n//10
print(opadajuce)

