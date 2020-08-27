rijec = input()
rijec = rijec.lower()
samoglasnici = "aeiou"
for i in range(1,len(rijec)):
    if rijec[i] in samoglasnici:
        pozicija = i
        break
nova_rijec = rijec[pozicija+1:] + rijec[: pozicija+1]
print(nova_rijec)
