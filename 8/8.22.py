tekst = input().lower()
tekst = tekst.split()
interpunkcija =",.?!"
brojac = 0
for element in tekst:
    e = element.strip(interpunkcija)
    if e[0] == e[-1]:
        brojac +=1
print(brojac)
