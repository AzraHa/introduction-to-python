m = int(input())
lista = []
for i in range(m):
    lista.append(int(input()))
lista.sort()
s1 = 0
s2 = 0
for i in range(m//2):
    s1 += lista[i]
for i in range(m//2,len(lista)):
    s2 += lista[i]
print(s2-s1, end = " ")
