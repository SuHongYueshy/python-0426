# 把一个tuple 转换成字符串
tuple = ('LiMing','Danny','Jenny')
print(tuple)    # 先输出一个tuple 与之后的字符串比较一下
str = ','.join(str(i) for i in tuple)  # 借用Join
print(str)