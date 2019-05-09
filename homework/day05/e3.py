# 斐波那契数列第N项
#    0，1，1，2，3，5，8，13，21，34

def fn_fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fn_fibonacci(n - 1) + fn_fibonacci(n - 2)
print(fn_fibonacci(15))
