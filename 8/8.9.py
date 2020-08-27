n = input()
lista = []
while n!="":
    if n[0]==n[len(n)-1] and n.count(n[0])==2:
        lista.append(n)
    n = input()

for el in lista:
    print(el,end = "\n")
