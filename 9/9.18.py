fajl = open("test01.in","r")
trgovci = dict()
automobili = dict()
for red in fajl:
    red = red.strip().split()
    if red[0] not in trgovci:
        trgovci[red[0]] = int(red[-1])
    else:
        trgovci[red[0]] += int(red[-1])
    if red[1] not in automobili:
        automobili[red[1]] = 1
    else:
        automobili[red[1]] += 1

tv = list(trgovci.values())
tk = list(trgovci.keys())

av = list(automobili.values())
ak = list(automobili.keys())
for i in range(3):
    print(tk[i],tv[i])
for i in  range(3):
    print(ak[i],av[i])
