# 输出内置函数
print(dir('__builtins__'))

#
print(abs(-1))

# 输出最大值
print(max(1,4))

# 输出最小值
print(min(1,2,3))

# n = float(input())
#
# print(n + 1)

print(str(123) + 'test')

a = [1, 2, 3, 1, 2, 3]

b = tuple(a)

print(b)

c = set(a)

print(c)

d = set(b)

print(c, d)

print(type(a), type(b), type(c), type(d))

absolute = abs

print(absolute(-1))


def add(x, y):
    return x + y


print(add(1, 2))


def test():
    pass
    # return


print(test())

# /**
#
# */


def multi_return(x, y):
    """
    :param x: int...
    :param y: float...
    :return: tuple...
    """
    return x, y


m, n = multi_return(1, 2)

print(m, n)

print(multi_return(3, 4))