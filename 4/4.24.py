m = int(input())
n = int(input())
for i in range(m):
    trenutni = 1
    for j in range(n):
        print(trenutni,end = " ")
        if trenutni == i+1:
            trenutni = 1
        else:
            trenutni +=1
    print()
