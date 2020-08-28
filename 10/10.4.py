def nadjiNajveci(lista):
    zadnji = lista.pop()
    if (len(lista) == 0):
        return zadnji
    return max(zadnji, nadjiNajveci(lista))
lista = []
n = int(input())
while n != -1:
    lista.append(n)
    n = int(input())
print(nadjiNajveci(lista))
