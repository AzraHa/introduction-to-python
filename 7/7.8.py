def obrnuta_cifra(broj):
    novi = 0
    while broj!=0:
        novi = novi*10 + broj%10
        broj //= 10
    return novi
n = input()
lista = []
while n!="":
    lista.append(int(n))
    n = input()
posljednji = lista[len(lista)-1]
if obrnuta_cifra(posljednji) in lista:
    print("DA")
else:
    print("NE")
