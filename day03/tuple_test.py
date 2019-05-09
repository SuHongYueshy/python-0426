names = ('LiMing','Danny','Jenny')  # 与列表不同的是，他是（）
print(names)

# 判断元素是否存在
print('LiMing' in names)
print('Tom' in names)
print('X' not in names)

# 元组长度
print(len(names))

# 元组构造器
names = tuple(('LiMing','Danny','Jenny'))
print(names)

# 将列表转换成元组
list = [1,2,4,6]
tuple = tuple(list)
print(tuple)

# 元素统计
print(names.count('LiMing'))

# 返回元素索引
print(names.index('LiMing'))

# 不可变的理解
superstars = ['Tom']
names = (superstars, 'Spike')  # <—— 说元组Names是不变的，而superstars的内容是个列表
print(names)
names[0].append('Jerry')      # names 的0下标是superstars，所以改变的是该列表的内容
print(names)

# 迭代
superstars = ['Tom']
names = (superstars,'Spike')
for name in names:
    print(name)