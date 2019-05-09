# for ... else    for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行
# 例1
for num in range(0, 10, 2):
    print(num)
else:
    print("输出的是偶数")

# 例2
fruits = ['apple', 'banana', 'orange']  # list 列表
# fruits = []  # list 列表
for fruit in fruits:
    print(fruit)
    if fruit == 'banana':
        break
else:  # 循环正常结束后的处理：没有 break
    print('else...')

is_found = False
for fruit in fruits:
    print(fruit)
    if fruit == 'watermelon':
        # proceed...
        print('found watermelon.')
        is_found = True
        break
# else:  # 循环正常结束后的处理：没有 break
#     print('not found watermelon.')

if not is_found:
    print('not found watermelon.')

# 语法糖 syntactic sugar: 在没有改变语言功能的前提下，是程序的写法更加简洁
# 语法： 盐/糖精/海洛因

# 习题2: for-else
for i in range(101,201):
    for j in range(2,i):
        if i%j==0:break
    else:
        print(i,'是质数')

for i in range(101,201):
    a=2
    while a<i: #
        if i%a==0:break
        else:a=a+1
    if a==i:
        print(i)