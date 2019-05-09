# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和。

n = 20

fenzi = 2  # 分子
fenmu = 1  # 分母
l = []
s = 0

for i in range(1, n + 1):
    a = fenzi
    b = fenmu

    s += (a / b)
    l.append('%s/%s' % (a, b))

    fenzi = a + b
    fenmu = a

print('+'.join(str(i) for i in l), end='')
print('=%.2f' % s)