def power(x):
    return x * x
print(power(2))

def power(x, n=3):
    p = 1
    while n > 0:
        p *= x
        n -= 1
    return p
print(power(2))


def fn_append(array=None):
    if array is None:
        array = []
    array.append('END')
    return array
print(fn_append([1, 2, 3]))
print(fn_append())  # ['END']
print(fn_append())  # ['END']
print(max(1, 2, 3, 4))
"""
void method(int... x)
"""


def fn_sum(*numbers):
    print(numbers)
    s = 0
    for n in numbers:
        s += n
    return s
print(fn_sum(1, 2, 3, 4, 5))
# print(fn_sum())


num = (1, 2, 3, 4, 5)
print(fn_sum(num[0], num[1], num[2], num[3], num[4]))
print(fn_sum(*num))


def fn_keywords(email, password, **kw):
    print(email, password)
    if 'gender' in kw:
        # todo
        pass
    if 'married' in kw:
        # todo
        pass


fn_keywords('tom@tom.com', 123, gender='male', married=False)

def fn_named_keywords(email, password, *, age, married=False, **kw):
    print(email, password, age, married, kw)

fn_named_keywords('jerry@tom.com', 'abc', age=18)
fn_named_keywords('jerry@tom.com', 'abc', age=18, married=True)
fn_named_keywords('jerry@tom.com', 'abc', age=18, married=True, gender='male')


def fn_named_keywords(email, password, *args, age, married=False, **kw):
    print(email, password, args, age, married, kw)


fn_named_keywords('email...', 'password...', 1, 2, 3, 'abc', age=19, gender='female')


def fn_test(a, b=1, *c, d, **e):
    print(a, b, c, d, e)
c = (3, 4, 5)
fn_test(1, *c, d=6)