# 输出规定格式的内容
print("""
      登鹳雀楼
      - 【唐】王之涣

      白日依山尽，
      黄河入海流。
      欲穷千里目，
      更上一层楼。
""")


# 输出Python 的版本号
import sys
print(sys.version)
print(sys.version_info)


# 格式化输出当前时间：年-月-日 时：分：秒
import datetime,time
now_time=datetime.datetime.now()
str_time=now_time.strftime("%Y-%m-%d %X")
print(str_time)


# 用户输入圆形半径，编写程序输出面积
import math
r = float(input('请输出圆的半径：'))
s = math.pi* r * r
print(s)


#isdigit() isnumeric() isdecimal() 的区别
# isdigit()  检测字符串是否只由数字组成
# isnumeric()  检测字符串是否只由数字组成
# isdecimal() 方法检查字符串是否只包含十进制字符



