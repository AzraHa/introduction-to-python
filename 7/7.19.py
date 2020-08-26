m = int(input())
n = int(input())
harun = []
sead = []
suma_harun = 0
suma_sead = 0
for i in range(m):
    a = int(input())
    harun.append(a)
    suma_harun += a
for i in range(n):
    b = int(input())
    sead.append(b)
    suma_sead += b
izbaciti = suma_sead-suma_harun
if izbaciti in sead:
    print("Jeste")
else:
    print("Nije")
