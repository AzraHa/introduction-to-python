def sumacifara(n):
    if n<10:
        return n
    return  n%10 + sumacifara(n//10)

n = int(input())
print(sumacifara(n))
