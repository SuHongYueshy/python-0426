# 按行读取一个文件，把每行内容存入一个 list

import sys
result=[]
with open('test.txt','r') as f:
 for line in f:
  result.append(list(line.strip('\n').split(',')))
print(result)

