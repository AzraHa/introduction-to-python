lista = input()
lista = lista.split()
lista = [int(x) for x in lista]
prvi = 0
posljednji = 0
for i in range(1,len(lista)-1):
    if(lista[i-1]<lista[i]) and (lista[i+1] < lista[i]):
        if prvi == 0:
            prvi = i
        zadnji = i
print(len(lista[prvi:zadnji+1]))
