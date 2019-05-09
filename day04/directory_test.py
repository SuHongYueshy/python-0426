import os

print(os.path.abspath('.'))  # 输出当前工作目录的绝对路径

print(os.getcwd())            # 同上

print(os.path.join('d:/test1','test2','test3'))  # 自动拼接路径

# print(os.mkdir(os.path.join('.','new_dir')))   # 创建目录

# print(os.rmdir(os.path.join('.','new_dir')))  # 删除目录

# print(os.makedirs(os.path.join('.','new_dir','sub_dir')))   #

print(os.path.split('new_dir/sub_dir/test.txt'))  # 拆分路径

print(os.path.splitext('google.com.png'))  # 输出扩展名

print([x for x in os.listdir('.') if os.path.isdir(x)])   # 目录列表



