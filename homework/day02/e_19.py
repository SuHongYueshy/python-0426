# 打印出如下图案（菱形）
for i in range(1, 5):
    for j in range(4 - i, 0, -1):
        print(' ', end='')
    for k in range(0, (i - 1) * 2):
        print('x', end='')
    print('x')

for i in range(1, 4):
    for j in range(0, i):
        print(' ', end='')
    for k in range(4, (i - 1) * 2, -1):
        print('x', end='')
    print('x')
