import random
fajl = open("test01.in","r")
random.seed(42)
n = int(fajl.readline().strip())
rijeci = []
rijec = fajl.readline().strip().lower()
while rijec != "":
    rijeci.append(rijec)
    rijec = fajl.readline().strip().lower()
lozinka = ""
for i in range(n):
    lozinka += rijeci[random.randrange(len(rijeci))]
print(lozinka)
