# list / tuple / dict / set
# 类型转换？
      #1、list、tuple是有序列表；dict、set是无序列表
      #2、list元素可变、tuple元素不可变
      #3、dict和set的key值不可变，唯一性
      #4、set只有key没有value
      #5、set的用途：去重、并集、交集等
      #6、list、tuple：+、*、索引、切片、检查成员等
      #7、dict查询效率高，但是消耗内存多；list、tuple查询效率低、但是消耗内存少

L = [1,2,3,4,5,6]
T = (4,7,2,8)
D = {0,4,1,9,6}
S = {3,1,99,43}

# 转元组
l = tuple(L)
print(l)

d = tuple(D)
print(d)

s = tuple(S)
print(s)

# 转列表
print(list(T))

print(list(D))

print(list(S))

# 转字典（元组不能转字典）
