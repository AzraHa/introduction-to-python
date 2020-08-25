n = int(input())

while n!=-1:
    hiljade = 0
    rezultat = ""
    while n!=0:
        rezultat = str(n%10) + rezultat
        print(rezultat)
        n = n//10
        hiljade += 1
        if n>0 and hiljade == 3:
            rezultat = "." + rezultat
            hiljade = 0
    print(rezultat)
    n = int(input())
