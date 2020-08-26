lista = input()
lista = lista.split()
lista = [int(x) for x in lista]
n = len(lista)
brojVecih = 0

for i in range(1,n):
    if lista[i] > lista[i-1]:
        brojVecih +=1
print(brojVecih)

brojVecihOdSume = 0
zbirPozitivnih = 0
if lista[-1] == 0:
    zbirPozitivnih = lista[-1]
for i in range(n-2,-1,-1):
    if lista[i] > zbirPozitivnih:
        brojVecihOdSume +=1
    if lista[i]>0:
        zbirPozitivnih+=lista[i]
print(brojVecihOdSume)
