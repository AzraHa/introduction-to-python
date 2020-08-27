tekst = input()
podvlacenje = ""
trenutno = ""

for slovo in tekst:
    if slovo.isalpha():
        trenutno += slovo
    else:
        if len(trenutno)>5:
            podvlacenje += "-"*len(trenutno)
        else:
            podvlacenje += " "*len(trenutno)
        podvlacenje += " "
        trenutno = ""
if len(trenutno)>5:
    podvlacenje += " " * len(trenutno)
else:
    podvlacenje += " "*len(trenutno)
trenutno = ""

print(tekst)
print(podvlacenje)
