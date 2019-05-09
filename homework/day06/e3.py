# 定义三角形类，实现求三角形周长和面积的方法，属性为三个边长

import math
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a+b>c and a+c>b and b+c>a:
    d=a+b+c
    e=(a+b+c)/2
    f=math.sqrt(e*(e-a)*(e-b)*(e-c))
    print('三角形的周长为：'+str(d))
    print('三角形的面积为：%f' % f)
else:
     print('三条变得长度不能构成三角形')