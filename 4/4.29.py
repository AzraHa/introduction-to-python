maxb = 0
maxn = 0
for i in range(1,10000):
    brojac = 1
    n = i
    while n!=1:
        if n%2 ==0:
            n //=2
        else:
            n = 3 * n + 1
        brojac +=1
    if(brojac>maxb):
        maxb = brojac
        maxn = i
print(maxn)
