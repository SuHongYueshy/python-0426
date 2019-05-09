# 求一个字符串 list 中，字符串长度大于2，且首尾字符相同的元素个数
# [‘a’, ‘xy’, ‘alabama’, ‘101’]
# 2

l = ['a','xy','alabama','101']
num = list(filter(lambda s:isinstance(s,str) and len(s) >= 2,l))
print(num)