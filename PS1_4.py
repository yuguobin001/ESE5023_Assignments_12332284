def dp(n):
    if n <= 3:
        return n - 1
    else:
        T = [0 for i in range(n + 1)]
        T[1], T[2], T[3] = 0, 1, 2
        for i in range(4, len(T)):
            if i % 2 != 0:
                T[i] = 1 + T[i - 1]
            else:
                T[i] = 1 + min(T[i - 1], T[int(i / 2)])
        return T[n]
print(dp(5))