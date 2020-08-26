lista = input()
lista = lista.split()
lista = [int(x) for x in lista]
#print("Lista: ",lista)
obrnuta = lista[::-1]
#print("obrnuta: ",obrnuta)
skup = set(lista)
#print("SKUP :" ,skup)
max_raspon = 0
for i in skup:
    start = lista.index(i)
    kraj = len(obrnuta) - obrnuta.index(i) - 1
    raspon = kraj - start + 1
    #print("Start: ",start," Kraj: ",kraj," Raspon: ",raspon,end = "\n")
    if raspon > max_raspon :
        max_raspon = raspon
print(max_raspon)
