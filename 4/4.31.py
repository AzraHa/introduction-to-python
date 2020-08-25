n = int(input())
brojKoraka = 0
listaPrethodnih = [n]
pojavilaSeJedinica = True
while n != 1:
    sumaKvadrataCifara = 0
    t = n
    while t > 0:
        sumaKvadrataCifara += (t % 10) * (t % 10)
        t = t // 10
    n = sumaKvadrataCifara
    if n in listaPrethodnih:
        print(-1)
        pojavilaSeJedinica = False
        break
    listaPrethodnih.append(n)
    brojKoraka += 1
if pojavilaSeJedinica:
    print(brojKoraka)
