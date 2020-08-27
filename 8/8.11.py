n = input()
n = n.lower()
str = "aeiou"
b = [0]*5
for s in n:
    if s == "a":
        b[0]+=1
    elif s == "e":
        b[1]+=1
    elif s == "i":
        b[2]+=1
    elif s == "o":
        b[3]+=1
    elif s == "u":
        b[4]+=1
print(str[b.index(max(b))])
