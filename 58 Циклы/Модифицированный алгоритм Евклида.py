a, b = sorted(list(map(int, input().split())), reverse=True)
iters = 0

# O(n // 100)
while b != 0:
    a, b = b, a % b
    iters += 1
print(a, iters)
