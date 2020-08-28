fajl = open("test01.in","r")
matrica = []
for red in fajl:
    red = red.strip().split()
    matrica.append(red)

redoviPalindromi = True
for i in range(len(matrica)):
    for j in range(len(matrica[i])//2):
        if matrica[i][j] != matrica[i][len(matrica)-1-j]:
            redoviPalindromi = False
kolonePalindromi = True
for i in range(len(matrica[0])):
    for j in range(len(matrica)//2):
        if matrica[j][i] != matrica[len(matrica)-1-j][i]:
            kolonePalindromi = False
if redoviPalindromi and kolonePalindromi:
    print("Savrsena")
elif redoviPalindromi or kolonePalindromi:
    print("Polusavrsena")
else:
    print("Nesavrsena")
