matrica = []
for i in range (3):
    red = input()
    matrica.append(red.split())

ispravna = True
for i in range(1,10):
    ponavljanja = sum(x.count(str(i)) for x in matrica)
    if ponavljanja != 1:
        ispravna = False
        break

for i in range(3):
    print(" ".join(map(str,matrica[i])))
print("ispravna " if ispravna else "neispravna")
