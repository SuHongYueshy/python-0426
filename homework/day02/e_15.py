# 输入三个整数x，y，z，请把这三个数由小到大输出。
# 我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
from pip._vendor.distlib.compat import raw_input

I = []
for i in range(3):
    x = int(raw_input(f'请输入一个整数：\n'))
    I.append(x)
    I.sort()
    print(I)