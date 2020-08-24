n = int(input())
if n>99 and n<1000:
    c = n%10
    n=n//10
    b=n%10
    n=n//10
    a=n%10

    print(a*b*c)
else:
    print("Pogresan unos")
