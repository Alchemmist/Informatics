n = int(input())
n = n - n % 2
for i in range(n, 0, -2):
    print(2 ** i, end=' ')
if n < 2:
    print(0)
