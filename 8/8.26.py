s1 = input().lower()
s2 = input().lower()

anagrami = True
for ch in s1:
    if ch.isalpha() and s1.count(ch) != s2.count(ch):
        anagrami = False

if anagrami:
    print("Anagrami")
else:
    print("Nisu anagrami")
