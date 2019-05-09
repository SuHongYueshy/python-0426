names = ['Tom','Jerry']

print(names)

print(names[0])

print(names[-1])   #  -1  输出数组的最后一个元素

print(names[-2])

# len() 方法返回列表元素个数。
print(len(names))

# append() 方法用于在列表末尾添加新的对象。
names.append('liming')
print(names)

# insert() 函数用于将指定对象插入列表的指定位置。
names.insert(1,'Danny')
print(names)

# 修改指定对象
names [3] = 'LiMing'
print(names)

# copy() 函数用于复制列表，类似于 a[:]。
name = names.copy()
print(name)

# 每行依次输出一个
for name in names:
    print(name)

# reverse() 函数用于反向列表中元素。
names.reverse()
print(names)

# sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数(按着字母顺序排序)
names.sort(reverse=True)
print(names)

# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
names.pop()  # 如果没有指定位置，默认是最后一个
print(names)

names.pop(0)  # 指定位置了，按指定的位置进行删除
print(names)

# clear() 函数用于清空列表，类似于 del a[:]。
superstars = ['Tom', 'Danny']
names = [superstars, 'Jerry']
names.clear()
print(names)
print(superstars == names)

# count() 方法用于统计某个元素在列表中出现的次数。
names.append('Tom')
print(names.count('Tom'))

# extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
superstars = ['Tom', 'Jerry']
names = ['Spike', 'Tyke']
superstars.extend(names)
print(superstars)

# index() 函数用于从列表中找出某个值第一个匹配项的索引位置。(下标)
print(names.index('Tyke'))

# remove() 函数用于移除列表中某个值的第一个匹配项。
names.remove('Spike')
print(names)




