# 添加元素   一次只能添加一个
keys = {'name','age'}
keys.add('gender')
print(keys)

# 删除指定元素
keys = {'name', 'age', 'married'}
keys.remove('married')  # keys.discard('married')
print(keys)

# 清空
keys = {'name', 'age', 'married'}
keys.clear()
print(keys)

# 拷贝
keys = {'name', 'age', 'married'}
new_keys = keys.copy()
print(new_keys)

# 随机删除元素
keys = {'name', 'age', 'married'}
new_keys = keys.pop()
print(new_keys)
print(keys)

# 返回差集
names1 = {'Tom', 'Jerry'}
names2 = {'Jerry', 'Spike'}
names3 = names1.difference(names2)
print(names3)

# 更新为差集
names1 = {'Tom', 'Jerry'}
names2 = {'Jerry', 'Spike'}
names1.difference_update(names2)
print(names1)

# 返回交集
names1 = {'Tom', 'Jerry'}
names2 = {'Jerry', 'Spike'}
names3 = names1.intersection(names2)
print(names3)

# 更新为交集
names1 = {'Tom', 'Jerry'}
names2 = {'Jerry', 'Spike'}
names1.intersection_update(names2)
print(names1)

#是否 不存在 交集
names1 = {'Tom', 'Jerry'}
names2 = {'Jerry', 'Spike'}
print(names1.isdisjoint(names2))

# 是否为子集
names1 = {'Tom', 'Jerry'}
names2 = {'Jerry', 'Spike'}
print(names1.issubset(names2))

# 是否为超集
names1 = {'Tom', 'Jerry'}
names2 = {'Jerry', 'Spike'}
print(names1.issuperset(names2))

# 返回对称差集
names1 = {'Tom', 'Jerry'}
names2 = {'Jerry', 'Spike'}
names3 = names1.symmetric_difference(names2)
print(names3)

# 更新为对称差集
names1 = {'Tom', 'Jerry'}
names2 = {'Jerry', 'Spike'}
names1.symmetric_difference_update(names2)
print(names1)

# 返回并集
names1 = {'Tom', 'Jerry'}
names2 = {'Jerry', 'Spike'}
names3 = names1.union(names2)
print(names3)

# 更新为并集
names1 = {'Tom', 'Jerry'}
names2 = {'Jerry', 'Spike'}
names1.update(names2)
print(names1)

# 集合运算
keys1 = {'name', 'age'}
keys2 = {'age', 'married'}
print(keys1 & keys2)
print(keys1 | keys2)

# 迭代
keys = {'name', 'age', 'married'}
for key in keys:
    print(key)



