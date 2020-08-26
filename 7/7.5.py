n = input()
lista = []
S = 0
B = 0
while n!="":
    lista.append(n)
    n = input()
for i in range(len(lista)):
    if lista[i][0] == "S":
        S +=1
    if lista[i][0] == "B":
        B +=1
if(S>B):
    for i in range(len(lista)):
        if lista[i][0] == "S":
            print(lista[i], end = " ")
elif B>S:
    for i in range(len(lista)):
        if lista[i][0] == "B":
            print(lista[i], end = " ")
else:
    for i in range(len(lista)):
         print(lista[i], end = " ")
