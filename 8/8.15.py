kartica = input()
grupe = len(kartica)//4
for i in range(grupe-1):
    print("****",end = " ")
print(kartica[-4:])
