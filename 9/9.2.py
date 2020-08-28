fajl = open("test01.in","r")
for red in fajl:
    red = red.strip().split()
    if red[0] == red[1] or len(red[1])<5 or "1234" in red[1]:
        print(red[0],red[1],end = "\n")
