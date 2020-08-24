n = int(input())
suma = 0
while n!=-1:
    if n>=10:
        n//=10
        suma+=n%10
    else:
        suma+=n
    n = int(input())
print(suma)
