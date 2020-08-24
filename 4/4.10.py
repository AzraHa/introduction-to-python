n = int(input())
brojac = 0
for i in range(n):
    rijec = input()
    if rijec == 'programiranje':
        brojac+=1
if brojac == 2:
    print("JESTE")
else:
    print("NIJE")
