fajl = open("test01.in","r")
red = fajl.readline().strip().split()
redovi = red[0]
kolone = red[1]
counts = dict()
for red in fajl:
    red = red.split()
    for element in red:
        counts[element] = counts.get(element,0)+1

s = [(k, counts[k]) for k in sorted(counts, key=counts.get, reverse=True)]
for i in range(3):
    print(s[i][0], s[i][1])
