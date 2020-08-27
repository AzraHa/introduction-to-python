string = input()
string = string.lower()
najduzi = 0
i = 0
while i<len(string):
    duzina = 0
    j = i
    while j<len(string) and string[j] == string[i]:
        duzina += 1
        j += 1
        if duzina > najduzi:
            najduzi = duzina
        i += duzina
print(najduzi)
