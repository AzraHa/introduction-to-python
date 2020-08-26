def rotiraj(broj):
    novi = 0
    while broj!=0:
        novi = novi* 10 + broj%10
        broj//=10
    return novi

n = int(input())
lista = []
lista_rotirani = []
while n!=-1:
    lista.append(n)
    lista_rotirani.append(rotiraj(n))
    n = int(input())
najveci = max(lista_rotirani)
najmanji = min(lista)
print(najveci-najmanji)


