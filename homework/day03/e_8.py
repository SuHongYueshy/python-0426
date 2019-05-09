# 找出两个 dict 中的 key-value 相同项
d1 = {'key1':1,'key2':3,'key3':2}
d2 = {'key1':1,'key3':3}

d3 = d1.items() & d2.items()
print(d3)