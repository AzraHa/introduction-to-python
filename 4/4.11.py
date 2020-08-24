poz1 = int(input())
skok1 = int(input())
poz2 = int(input())
skok2 = int(input())
poz3 = int(input())
skok3 = int(input())
cilj = int(input())
max = 0

while True:
    poz1 += skok1
    if poz1 >= cilj:
        max = poz1
        break;
    poz2 += skok2
    if poz2 >= cilj:
        max = poz2
        break;
    poz3 += skok3
    if poz3 >= cilj:
        max = poz3
        break
for i in range(1, max+1):
    if i != cilj and i != poz1:
        print("-", end="")
    elif i == poz1:
        print("*", end="")
    else:
        print("|", end="")
print()

for i in range(1, max+1):
    if i != cilj and i != poz2:
        print("-", end="")
    elif i == poz2:
        print("*", end="")
    else:
        print("|", end="")
print()
for i in range(1, max+1):
    if i != cilj and i != poz3:
        print("-", end="")
    elif i == poz3:
        print("*", end="")
    else:
        print("|", end="")
print()

