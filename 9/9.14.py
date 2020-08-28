matrica = []
with open("test01.in","r") as f:
    for red in f:
        red = red.strip().split()
        matrica.append(red)
sirina = len(matrica[0])
visina = len(matrica)
nova = []
for i in range(visina):
    red = ["-"] * sirina
    nova.append(red)
for j in range(sirina):
    kolona = []
    for i in range(visina):
        kolona.append(matrica[i][j])
    for i in range(visina):
        if matrica[i][j] == "#":
           nova[i][j] = "#"
        elif "#" in matrica[i][:j] and "#" in matrica[i][j:] and "#" in kolona[:i] and "#" in kolona[i:]:
            nova[i][j] = "#"
brojac = 0
for red in nova:
    for kolona in red:
        if kolona == "#":
            brojac += 1
print(brojac)
