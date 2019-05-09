# 把一个 dict 按 key 排序输出
d = {'name': 'Danny', 'age': '18', 'gender': 'male', 'married': False}
d = sorted(d.items(),key = lambda k : k[0])
print(d)

d = {'name':'Danny','age':'12','married':'True'}
print(d.keys())
