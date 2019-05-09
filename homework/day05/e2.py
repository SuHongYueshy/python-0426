# 定义函数，把一个list的元素去重，返回新的List

ids = [1,2,3,3,4,2,3,4,5,6,1]
news_ids = []
for id in ids:
    if id not in news_ids:
        news_ids.append(id)
print (news_ids)