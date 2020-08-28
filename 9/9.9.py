fajl = open("test01.in","r")
mjeseci = ["Januar","Februar","Mart","April","Maj","Juni","Juli","August","Septembar","Oktobar","Novembar","Decembar"]
suma = 0
matrica = []
prosjecne = []
for red in fajl:
    red = red.split()
    matrica.append(red)
for i in range(12):
    for j in range(5):
        suma += float(matrica[j][0])
    prosjecne.append(suma/5)
for i in range(11):
    print(prosjecne[i],end = ",")
print(prosjecne[-1])
najveca = prosjecne.index(max(prosjecne))
najmanja = prosjecne.index(min(prosjecne))
print(mjeseci[najmanja],mjeseci[najveca],end =" \n")


