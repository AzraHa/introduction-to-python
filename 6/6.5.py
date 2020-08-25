def spirala(n):
    for i in range (1, n+1):
        for j in range (1, n+1):
        # okvir u kojem crtamo
            N = min(i, j, (n - i + 1), (n - j + 1)) - 1
            if N == i-1:
                poz = j - N
            elif N == n - j:
                poz = (j - N) + (i - N) - 1
            elif N == n - i:
                poz = (2 * (n - 2 * N) - 1) + ((n - j + 1) - N) - 1
            elif N == j - 1:
                poz = (3 * (n - 2 * N) - 2) + ((n - i + 1) - N) - 1
            print("%3s" % int((2 * n * N) + (2 * N * (n - 2 * N)) +poz), end=" ")
        print()
n=int(input())
spirala(n)
