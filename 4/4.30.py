n = int(input())
print("   ", end="")
for i in range(1, n+1):
    if i < 10:
        print(" ", end = "")
    print(str(i), end = "  ")
print()
for i in range(1, n+1):
    if i < 10:
        print(" ", end = "")
    print(i, end = "")
    for j in range(1, n+1):
        if i * j < 10:
            print(" ", end = "")
        if(i * j < 100):
            print(" ", end = "")
        print(str(i * j), end= " ")
    print()
