def s(n):
    if n == 0:
        return 0
    return s(n-1) + 1 / (n**3 + n)
n = int(input())
print(s(n))
