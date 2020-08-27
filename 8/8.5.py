n = input()
m = int(input())
dec = n[:len(n)-m] + "." + n[len(n)-m:]
print(dec)
