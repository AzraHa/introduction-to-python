n = int(input())
max_raspon = 0
t_raspon = 0
while n>0:
    cifra = n%10
    if cifra<5:
        if t_raspon>max_raspon:
            max_raspon = t_raspon
        t_raspon = 0
    else:
        t_raspon += 1
    n //= 10
if t_raspon>max_raspon:
    max_raspon = t_raspon
print(max_raspon)

