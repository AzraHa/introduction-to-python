def f(n):
    while n>9:
        suma = 0
        while n >0:
            suma += n%10
            n //=10
        n = suma
    return suma


