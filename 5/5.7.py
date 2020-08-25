import random
broj_simulacija = 10000
broj_uspjeha = 0
for i in range(broj_simulacija):
    a = random.randint(1,1000)
    b = random.randint(1,1000)
    c = random.randint(1,1000)
    ostrougli = True
    if a+b<=c or b+c<=a or a+c<=b:
        ostrougli = False
    if(a*a + b*b <= c*c or a*a + c*c <= b*b or b*b + c*c <= a*a):
        ostrougli = False
    if ostrougli:
        broj_uspjeha +=1

print(100.0 * broj_uspjeha / broj_simulacija)

