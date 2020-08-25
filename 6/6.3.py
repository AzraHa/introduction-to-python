def f(a,b):
    temp = b
    desetine = 1
    while temp != 0:
        desetine *= 10
        temp //= 10
    seNalazi = False
    while a != 0:
        temp = a % desetine
        if temp == b:
            seNalazi = True
            break
        a //= 10
    if seNalazi:
        print("Nalazi se")
    else:
        print("Ne nalazi se")

f(123456,234)
