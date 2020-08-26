lista = input()
lista = lista.split()
lista = [int(x) for x in lista]

najduza_sekvenca = 0

for i in range(len(lista)):
    for j in range(len(lista)):
        pocetak = i
        kraj = j
        preklapanje = 0
        while pocetak<len(lista) and kraj>=0 and lista[pocetak] == lista[kraj]:
            pocetak +=1
            kraj -=1
            preklapanje +=1
        najduza_sekvenca = max(najduza_sekvenca,preklapanje)
print(najduza_sekvenca)
