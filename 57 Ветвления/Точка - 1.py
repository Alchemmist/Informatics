x, y = map(float, input().split())
if (x ** 2 + y ** 2 > 4) and \
   (y < x) and \
   (x < 2) and \
    y > 0:
    print('YES')
else:
    print('NO')


