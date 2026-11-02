A = [4, 7, 2, 9]
jam = 0

for i in range(len(A)):
    if A[i] % 2 == 0:
        jam = jam + A[i]

print("Sum =", jam)
