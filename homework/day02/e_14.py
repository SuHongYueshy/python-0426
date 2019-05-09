# 输入某年某月某日，判断这一天是这一年的第几天？(闰年： 西元年份除以400余数为0的，或者除以4为余数0且除以100不为余数0的，为闰年。)
# 以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于3时需考虑多加一天。
def leapyear(y):
    return (y % 400 == 0 or (y % 4 ==0 and y % 100 ==0))
days = [0,31,28,31,30,31,30,31,31,30,31,30]
res = 0
year = int(input("year："))
month = int(input("month："))
day = int(input("day："))
if leapyear(year):
    days[2] += 1
for i in range(month):
    res += days[i]
print(f"这是{year}年的第{res+day}天")


