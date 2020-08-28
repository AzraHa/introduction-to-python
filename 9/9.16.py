def u_minute(vin):
    vt = list(vin)
    mins_lista = []
    for v in vt:
        if v[0] == "12":
            v[0] = "0"
        mins = int(v[0]) * 60 + int(v[1]) + 60 * 12 * (1 if v[2].lower() == "pm" else 0)
        mins_lista.append(mins)
    return mins_lista

def u_sate(mins_lista_in):
    mli = list(mins_lista_in)
    vremena = []
    for mins in mli:
        oznaka = "AM"
        sati = mins // 60
        if sati > 11:
            sati = sati - 12
            oznaka = "PM"
        if sati == 0:
            sati = 12
            minute = mins % 60
            sati = str(sati)
            minute = str(minute)
        if len(sati) < 2:
            sati = "0" + sati
        if len(minute) < 2:
            minute = "0" + minute
        vremena.append(sati + ":" + minute + " "+ oznaka)
    return vremena

vremena_in = []
with open("test01.in","r") as f:
    vremena_in = list(f)

vremena_minute = u_minute(vremena_in)
vremena_minute.sort()
vremena_out = u_sate(vremena_minute)

for v in vremena_out:
    print(v)
