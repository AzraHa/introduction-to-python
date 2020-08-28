def s(n):
    if n == 0:
        return 0
    return s(n-1) + n*n
n = int(input())
print(s(n))
