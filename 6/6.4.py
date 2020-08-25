def suma_na_dijagonalama(n):
    if n == 1:
        return 1
    suma = 1
    for i in range(2, int((n+1)/2)+1):
        suma += (2 * i - 1) ** 2
        suma += (2 * i - 1) ** 2 - (2 * i - 2)
        suma += (2 * i - 1) ** 2 - 3 * (2 * i - 2)
        suma += (2 * i - 1) ** 2 - 2 * (2 * i - 2)
    return suma
n=int(input())
print(suma_na_dijagonalama(n))
