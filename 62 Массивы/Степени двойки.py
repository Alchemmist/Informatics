n = int(input())
print(*[2 ** i for i in range(1, n + 1)][::-1])
