n = input()
lista_rijeci = []
samoglasnici ="aeiou"
nova_rijec =""
while n!="":
    for i in range(len(n)):
        if n[i] not in samoglasnici:
            nova_rijec += n[i]
    lista_rijeci.append(nova_rijec)
    nova_rijec = ""
    n = input()
for rijec in lista_rijeci:
    print(rijec,end = " ")
