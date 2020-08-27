n = int(input())
najduzi = 0
najkraci = 101
for i in range(n):
    s = input()
    if len(s) % 2 == 1 and len(s) > najduzi:
        print(s)
    elif len(s) % 2 == 0 and len(s) < najkraci:
        print(s)
    if len(s) > najduzi:
        najduzi = len(s)
    if len(s) < najkraci:
        najkraci = len(s)

