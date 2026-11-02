def Tarkib(n, k):
    if k == 0 or k == n:
        return 1
    return Tarkib(n - 1, k - 1) + Tarkib(n - 1, k)
