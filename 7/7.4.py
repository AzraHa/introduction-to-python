lista = []
n = input()
while n!="":
    lista.append(int(n))
    n = input()
l_najmanji = [] + lista[:len(lista)//2]
l_najmanji.sort()
l_najveci = [] + lista[len(lista)//2:]
l_najveci.sort()
najmanji = l_najmanji[0]
najveci = l_najveci[len(l_najveci)-1]
for i in range(najmanji,najveci+1,2):
    print(i,end = " ")
