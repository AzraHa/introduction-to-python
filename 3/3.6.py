x = int(input())
if x > 9999 and x < 100000:
        e = x % 10
        x = x // 10
        d = x % 10
        x = x // 10
        c = x % 10
        x = x // 10
        b = x % 10
        x = x // 10
        a = x
        tmax = a
        if b > tmax:
            tmax = b
        if c > tmax:
            tmax = c
        if d > tmax:
            tmax = d
        if e > tmax:
            tmax = e
        tmin = a
        if b < tmin:
            tmin = b
        if c < tmin:
            tmin = c
        if d < tmin:
            tmin = d
        if e < tmin:
            tmin = e
        print(tmax - tmin)
else:
    print("Pogresan unos!")
