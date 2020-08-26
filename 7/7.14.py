def postavi_cifre(n,c): #kreira listu [0,1,2,3,4,5,6,7,8,9]
    for i in range(10): # tj. [False,False,...]
        if str(i) in str(n):
            c[i] = True

n1 = int(input())
cifre = [False] * 10
postavi_cifre(n1,cifre) #ubacuje cifre broja n1 u listu

while False in cifre:
    n2 = n1
    zbir = 0
    while n1 > 0:
        zbir += n1%10
        n1//=10
    n2 = int(str(n2)+str(zbir))
    postavi_cifre(n2,cifre)
    n1 = n2
print(n1)

