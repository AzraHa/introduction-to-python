n = int(input())
s = 1
while s%n != 0:
    s = s*10 +1

print(len(str(s)))
