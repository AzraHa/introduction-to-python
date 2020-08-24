n = int(input())
najveca = n%10
najmanja = n%10

while n!=0:
    cifra = n%10
    if cifra>najveca:
        najveca = cifra
    if cifra<najmanja:
        najmanja = cifra
    n//= 10

print(najveca*najmanja - najveca/najmanja)

