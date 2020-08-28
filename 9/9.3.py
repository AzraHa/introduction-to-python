fajl = open("test01.in","r")
lista1 = []
lista2 = []
lista3 = []
for red in fajl:
    red = red.strip()
    if red[-1] == "3":
        lista3.append(red[:-2])
    if red[-1] == "2":
        lista2.append(red[:-2])
    if red[-1] == "1":
        lista1.append(red[:-2])

for el in lista1:
    print(el)
print()
for el in lista2:
    print(el)
print()
for el in lista3:
    print(el)
