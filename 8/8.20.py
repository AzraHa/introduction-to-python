unos = input()
ispis = unos.replace(" i "," I ")
print(ispis)
for i in range(len(unos)):
    if unos[i] != ispis[i]:
        print("_",end="")
    else:
        print(" ",end="")
