# 读取一个文本文件的前 N 行

f = open('D:/test.py', encoding='utf-8')
for i in range(4):
    print(f.readline().strip())