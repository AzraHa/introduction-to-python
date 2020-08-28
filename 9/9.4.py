fajl= open("test01.in","r")
matrica = []
suma = 0
for red in fajl:
    red = red.strip().split()
    matrica.append(red)
m1 = matrica[:len(matrica)//2]
m2 = matrica[len(matrica)//2:]

for i in range(len(m1)):
    for j in range(len(m2)):
        broj = int(m1[i][j])
        if m2[i][j] == "*" and broj %2 == 0:
            suma += broj
print(suma)
