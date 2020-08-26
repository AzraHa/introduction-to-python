n = input()
lista = []
while n!="":
    lista.append(int(n))
    n = input()
parni = []
neparni = []
neparni_index = []
for i in range(len(lista)):
    if lista[i]%2 == 0:
        parni.append(lista[i])
    else:
        neparni.append(lista[i])
        neparni_index.append(i)
parni.sort()
sortirana = [0]*len(lista)
for i in range(len(neparni)):
    sortirana[neparni_index[i]] = neparni[i]
j = 0
for i in range(len(sortirana)):
    if sortirana[i]==0:
        sortirana[i] = parni[j]
        j +=1

print(sortirana)
