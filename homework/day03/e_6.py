# 把 3 个 dict 合并为 1 个 dict
d1 = {'name':'Danny'}
d2 = {'age':'18'}
d3 = {'gender':'male','married':False}
d4 = {}
for k,v in d1.items():
    d4[k] = v
    for k,v in d2.items():
        d4[k] = v
        for k,v in d3.items():
            d4[k] = v
            print(d4)

#  update()
d1 = {'name':'Danny'}
d2 = {'age':'18'}
d3 = {'gender':'male','married':False}
d4 = {}
d4.update(d1)
d4.update(d2)
d4.update(d3)
print(d4)