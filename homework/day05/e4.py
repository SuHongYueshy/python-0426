# 汉诺塔N圆盘移动步骤
# n = 2
# A - B
# A - C
# B - C


def hanoi(n,A,B,C):
    if n==1:
        print(A,"-->",C)
    else:
        hanoi(n-1,A,C,B)
        print(A,"-->",B)
        hanoi(n-1,B,A,C)
while True:
    n=int(input("n == "))
    hanoi(n,'A','B','C')

