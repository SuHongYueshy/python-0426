s = 'Hello,World!'
a = '123'
b = '1111SHY!11111'

# []  输出对应下标
print(s[0])

# +  连接
txt1 = 'Hello,'
txt2 = 'World!'
print(txt1 + txt2)

# *
print(s * 3)

#[:[step]]
print(s[5:7])

# in 判断''内的东西是否存在
print('s' in s)

# not in
print('H' not in s)

# capitalize()
print(s.capitalize())

# center(width[, fillchar])  zfill()
print(s.center(20,'-'))
print(s.zfill(20)) #  zero fill

# count 找数量
print(s.count('l'))

# endswith 判断结尾是否正确
print(s.endswith('!', 0, 1))

# find 查找东西
print(s.find(',', 10, 13))

# isalnum()  检测字符串是否由字母和数字组成
print(s.isalnum())

# isalpha()  检测字符串是否只由字母组成。
print(s.isalpha())

# isdigit()  检测字符串是否只由数字组成
print(s.isdigit())


# islower()  检测字符串是否由小写字母组成。
print(s.islower())

# str.isupper()  检测字符串中所有的字母是否都为大写
print(s.isupper())

# isnumeric()  检测字符串是否只由数字组成。这种方法是只针对unicode对象
print(s.isnumeric())

# isspace()  检测字符串是否只由空格组成


# str.join(sequence)  将序列中的元素以指定的字符连接生成一个新的字符串
print(s.join(a))

# len(string)  输出字符串长度
print(len(s))

# lower() 转换字符串中所有大写字符为小写
print(s.lower())

# upper()  转换字符串中所有小写字符为大写
print(s.upper())

# swapcase()  对字符串的大小写字母进行转换
print(s.swapcase())

# lstrip()  截掉字符串左边的空格或指定字符
print(b.lstrip('1'))

# rstrip() 截掉字符串右边的空格或指定字符
print(b.rstrip('1'))

# strip() 移除字符串头尾指定的字符（默认为空格）或字符序列


# max(str)  返回字符串中最大的字母
print(max(s))

# min(str)  返回字符串中最小的字母
print(min(s))

# replace(old, new [, max])  字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
print('输出的语句是：',s)
print('输出的语句是：',s.replace(s,a))

#  str()  将对象转化为适于人阅读的形式

