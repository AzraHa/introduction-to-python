fajl = open("test01.in","r")
dan = -1
najvecaT = -1000
najveci_dan = ""
najveci_grad = ""
najmanjaT = 1000
najmanji_dan = ""
najmanji_grad =""
dani = ["ponedjeljak", "utorak", "srijeda","cetvrtak", "petak", "subota", "nedjelja"]
red = fajl.readline()
while red != "":
    if(len(red))==2:
        dan += 1
        red = fajl.readline()
    else:
        red_lista = red.split()
        temp = float(red_lista[-1])
        grad = red_lista[0]
        for i in range(1, len(red_lista) - 1):
            grad += " " + red_lista[i]
        if temp > najvecaT:
            najvecaT = temp
            najveci_grad = grad
            najveci_dan = dani[dan]
        elif temp< najmanjaT:
            najmanjaT = temp
            najmanji_grad = grad
            najmanji_dan = dani[dan]
        red = fajl.readline()
print(najmanji_grad,najmanjaT,najmanji_dan)
print(najveci_grad,najvecaT,najveci_dan)

