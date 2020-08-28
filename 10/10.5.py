def najkraca(i, j):
    suma = matrica[i][j]
    if i == br_redova-1 and j == br_kolona-1:
        return matrica[i][j]
    elif i == br_redova-1:
        return matrica[i][j] + najkraca(i, j+1)
    elif j == br_kolona-1:
        return matrica[i][j] + najkraca(i+1, j)
    else:
        return matrica[i][j] + min(najkraca(i+1, j),najkraca(i, j+1))

matrica = []

for i in range(4):
    red = input()
    red = red.split()
    red = [int(x) for x in red]
    matrica.append(red)

br_redova = len(matrica)
br_kolona = len(matrica[0])
print(najkraca(0,0))
