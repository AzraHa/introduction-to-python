n = int( input())
p = 1
while n!=0:
    cifra = n%10
    if cifra%2 != 0 and cifra<6:
        p = p*cifra
    n = n//10

print(p)
