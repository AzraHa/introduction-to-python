recenica = input()
recenica = recenica.upper()
if recenica.count("A")> recenica.count("E"):
    print("A")
elif recenica.count("A")<recenica.count("E"):
    print("E")
else:
    print("AE")
