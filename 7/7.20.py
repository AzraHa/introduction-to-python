m = int(input())
brojevi =  []
for i in range(m):
    brojevi.append(int(input()))
parovi = []
m = int(input())
while m!=-1:
    p1 = m
    p2 = int(input())
    parovi.append([p1,p2])
    m = int(input())
for par in parovi:
    temp = brojevi[par[0]]
    brojevi[par[0]] = brojevi[par[1]]
    brojevi[par[1]] = temp

for e in brojevi:
    print(e,end =" ")

