lista = input()
lista = lista.split(", ")
recenica = input()
for rijec in lista:
    recenica = recenica.replace(rijec,"*"*len(rijec))
print(recenica)
