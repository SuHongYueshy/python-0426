# 实现Power的功能  pow(x,n)函数(求x的n次方)
class Solution:
    def power(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            x = 1/x
            n = -n
        ans = 1.0
        while n > 0:
            if n&1 :
                ans *= x
            x *= x
            n >>= 1
        return ans

print(Solution().power(2,-3))
print(Solution().power(3, 5))
print(Solution().power(100, 0))