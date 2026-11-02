def Akerman(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return Akerman(m - 1, 1)
    return Akerman(m - 1, Akerman(m, n - 1))
