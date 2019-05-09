d = {'name':'Tom','age':'18','gender':'male','isMarried':False}

# 输出整个字典
print(d)

# 输出特定的内容
print(d['name'])

# 声明
d = {}
d = dict()

# 初始化
d = dict(key = 123)  # Constructor
d ['test_key'] = False
d['key'] = 'value'
   # fromkeys
d = {}.fromkeys(['name','age'])
print(d)
d = {}.fromkeys(['name','age'],'value')
print(d)

# 获取键对应的值
d = {'key':'value'}
print(d['key'])
   #get 方法
print(d.get('key1'))
print(d.get('key1','new value'))

# 更新
d = {'key':'value'}
d['key'] = 'updated value'
d['new key'] = 'new value'
print(d)
   # update方法
d.update({'name':'Danny'})
print(d)
d.update({'age':'20'})
print(d)

# 删除
d = {'name':'Jenny','age':'16','married':False}
del d['age']
d.pop('married')
d.popitem()   # 删除掉最后一个
print(d)

# 清空
d ={'name':'Danny','age':'12','married':'True'}
d.clear()
print(d)

# 输出dict的长度
d = {'name':'X','age':'29','married':'False'}
print(len(d))

# 拷贝
d = {'name':'Danny','age':'12','married':'True'}
b = d.copy()
print(b)

# 迭代
d = {'name':'Danny','age':'12','married':'True'}
print(d.keys())

for key in d:
    print(key)
    for value in d.values():
        print(value)
        for key,value in d.items():
            print(key,':',value)

import collections
d = collections.OrderedDict()
d = {'k1': 'v1', 'k2': 'v2'}
for key in d:
    print(key, d[key])