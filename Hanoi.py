def Hanoi(n, mabda, maghsad, komaki):
    if n == 1:
        print(mabda, "->", maghsad)
        return

    Hanoi(n - 1, mabda, komaki, maghsad)
    print(mabda, "->", maghsad)
    Hanoi(n - 1, komaki, maghsad, mabda)
