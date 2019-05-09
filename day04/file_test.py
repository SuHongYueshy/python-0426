import os
import shutil
#os.remove('test.txt')   # 删除

if os.path.exists('test.txt'):   # 判断有无文件
    os.remove('test.txt')
else:
    print('not exist!')

#os.rename('download.py','download_test.py')  # 更改文件名

#shutil.copy('file_test.py','file_test_new.py')  # 复制一个文件（借用shutil的copy函数）

# split.ext : extension 扩展名
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])   # 列表生成器

print(os.path.splitext('file_test.py'))   # 转换成了元组







