fajl = open("test01.in","r")
sekvenca = fajl.readline()
najduza = ""
duzina = 0
index1 = sekvenca.find("AGGT")
while index1!=-1:
    sekvenca = sekvenca[index1+4:]
    index2 = sekvenca.find("AGGT")
    if index2 != -1:
        podsekvenca = sekvenca[:index2]
        if len(podsekvenca)>duzina:
            duzina = len(podsekvenca)
            najduza = podsekvenca
    index1 = index2
print(najduza)
