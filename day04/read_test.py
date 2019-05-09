# 读文件
from urllib.request import urlopen

f = open('D:/test.py',encoding='utf-8')
print(f.read())
f.close()

# 读出指定内容
with open('D:/test.py',encoding='utf-8') as f:
    print(f.read(2))

# 读出全部内容
with open('D:/test.py',encoding='utf-8') as f:  # 因为后面有冒号所以必须有内容，如果没有内容，可以直接打一个Pass
    print(f.read())

#
with open('D:/test.py', encoding='utf-8') as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()

s = ' Hello, World! '
print(s.strip())
print(s.lstrip())  # l:去掉left的空格
print(s.rstrip())  # r:去掉right空格


with open('D:/test.py', encoding='utf-8') as f:
    for x in f:
        print(x.strip())


with open('D:/test.py', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())

# 输出二进制
#import os
#print(os.getcwd())    查找现在运行的目录
with open('1.jpg','rb') as f:
    print(f.read())      # 图片以二进制形式输出

# 输出一个网络文件
with urlopen('https://book.douban.com/subject/1005022/') as f:
    for line in f.readlines():
        print(line.decode('UTF-8').strip())

# 展示豆瓣的图片
with urlopen('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4') as f:
    for line in f.readlines():
        line = line.decode('utf-8')
        if 'img class=""' in line:
            print(line.strip()[len('<img class="" src="'):len(line.strip())-1])

