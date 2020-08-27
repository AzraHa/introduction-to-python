n = input()
lista = []
while n!="":
    srednji = n[len(n)//2]
    srednji = int(srednji)
    if srednji > 5:
        lista.append(n)
    n = input()
for element in lista:
    print(element , end = " ")
