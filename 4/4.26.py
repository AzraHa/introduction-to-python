a = int(input())
b = int(input())
for i in range(a,b+1):
    cifra = False
    n = i
    while n!=0:
        c = i%10
        if c%3 == 0:
            cifra = True
        n //=10
    if i%3 == 0 or cifra == True:
        print(i,end = " ")

