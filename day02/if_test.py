score = 70

if score > 60:
    print('pass')

if score > 60:
    print('pass')
else:
    print('failed')

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
else:
    print('C')


print('x')
print('x')

# python 不换行输出 x ？

for y in range(4,-5,-1):
    for x in range(-4,5):
        if abs(x)+abs(y)<=4:
            print('x',end ='')
        else:
            print(' ',end ='')
    print()