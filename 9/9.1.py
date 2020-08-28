fajl = open("test01.in","r")
matrica = []
suma = 0
for red in fajl:
    suma += sum(float(x) for x in red.strip().split())
print(suma)
