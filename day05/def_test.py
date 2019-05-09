from day05.build_in_test import multi_return

print(multi_return(1, 2))


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Error...')  # throw
    if x > 0:
        return x
    else:
        return -x


# print(my_abs(-1))
print(my_abs('-1'))