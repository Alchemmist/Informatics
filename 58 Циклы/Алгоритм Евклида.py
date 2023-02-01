a, b = sorted(list(map(int, input().split())), reverse=True)
iters = 0

# O(n // 100)
# while b != 0: 
#     a, b = b, a % b 
#     iters += 1
# print(a, iters)


# O(n)
while a != 0 and b != 0:
    if a > b: 
        a = a - b
        iters += 1
    else: 
        b = b - a 
        iters += 1

print(max(a, b), iters)

