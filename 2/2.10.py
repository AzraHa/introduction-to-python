import math
L = float(input())
n = float(input())
k = float(input())
h = float(input())

brojnik = 2 * k **(2/3) * math.cos(math.radians((L)))
nazivnik = math.sin(math.radians((L))) * math.sqrt(h+n)

print(brojnik/nazivnik)
