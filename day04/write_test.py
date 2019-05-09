with open('test.txt','w') as f:
    f.write('Hello ,World!')

with open('test.txt','a') as f:
    f.write('Hello,Java!')

with open('test_new.txt','x') as f:  # x 必须新建一个才可以添加
    f.write('Hello,Python!')

# 二进制
with open('1.jpg','rb') as f1:
    with open('2.jpg','wb') as f2:
        f2.write(f1.read())