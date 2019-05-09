# 定义函数，统计一个字符串在大写，小写字母的个数


def statistic_string(ostr):
    uppers = 0
    lowers = 0
    odict = {}

    for istr in ostr:
        if istr.isupper():
            uppers += 1
        elif istr.islower():
            lowers += 1
    else:
        odict.setdefault('大写字母个数', uppers)
        odict.setdefault('小写字母个数', lowers)
    return odict

if __name__ == '__main__':
    astr = 'hsheSHHUG123$#%^^&'
    print(statistic_string(astr))
