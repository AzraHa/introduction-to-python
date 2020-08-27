stih = input()
lista = []
while stih!="":
    lista.append(stih)
    stih = input()

ispis = ""
for i in range(len(lista)):
    ispis += lista[i][i]
print(ispis)
