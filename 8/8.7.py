s = input()
zbir = 0
while len(s) == 1:
    if s.isnumeric():
        i = int(s)
        if i % 2 == 0:
            zbir += i
    s = input()
print(zbir)
