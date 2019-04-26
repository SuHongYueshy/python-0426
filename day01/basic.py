'''
multiple line comment
'''

""""
multple line comment
"""

# data type     Python没有数据类型
# 整形 int
x = 3
print(x)

# HEX 十六进制
print(0xff)

# 浮点数 float
print(1.23E4)

# 复数 complex 实部和虚部都是浮点数
print('complex', 1+2j)
print(complex(1,2))
print('complex',complex(1,2).conjugate())

# 字符串
print('abcd')

# \ 转义字符
print('Tom \'s name')
print(r'Tom \'s name')

# \n 换行
print('line\nanother line')

print('''line
another line''')

print("""
床前明月光，
疑是地上霜。
""")

print(r'''line \n
another line''')

# output  print
print('test')
print('a','bb','ccc')
print(1 + 1)

name = input()
print(name)

# Scanner
"""
Scanner scanner = new Scanner(System.in);
int i = scanner.nextInt();
System.out.println(i);
// 123
"""

print(input())

"""
class test {
    void method(){
        for(int i=0; i<10; i++) {

        }
    }
}
"""

#r/R  原始字符串 - 原始字符串
print (r'\n')
print(R'\n')

# %  格式字符串


class test:
    def fun(self):
        for i in range(10):
            print(i)