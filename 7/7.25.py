n = int(input())
matrica = []
for i in range(n):
    red = []
    for j in range(n):
        red.append(int(input()))
    matrica.append(red)

for i in range(n):
    for j in range(n):
        for k in range(n-1):
            if matrica[k][i] > matrica[k+1][i]:
                temp = matrica[k][i]
                matrica[k][i] = matrica[k+1][i]
                matrica[k+1][i] = temp

for i in range(n):
    for j in range(n):
        print(matrica[i][j],end = " ")
    print()
