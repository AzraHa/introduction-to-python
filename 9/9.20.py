fajl = open("test01.in","r")
red = fajl.readline()
while red != "":
    ucenik = red.strip()
    uspjeh = 0
    predmeti = []
    for i in range(3):
        p,o = fajl.readline().strip().split()
        o = int(o)
        if o == 1:
            predmeti.append(p)
        uspjeh += o
    print(ucenik,end = " ")
    if(len(predmeti)==0):
        print(uspjeh/3)
    else:
        for predmet in predmeti:
            print(predmet, end = " ")
        print()
    red = fajl.readline()
