"""
Given a 32-bit signed integer, reverse digits of an integer.
Input: 123
Output: 321

Input: -123
Output: -321

Input: 120
Output: 21

Input: 1534236469
Output: 0

Assume we are dealing with an environment which could only store integers 
within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose 
of this problem, assume that your function returns 0 when the reversed integer 
overflows.

nnd,复制题目的时候把界 2^31变成了 231



"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        num = []
        res = ''
        flag = 0
        if x == 0 :
            return 0
        if x < 0:
            flag = 1
            x = - x
        while x > 0:
            r = int(x % 10)
            num.append(r)
            res += str(r)
            x = int(x / 10)
        res = int(res)
        if res < (-2**31) or res > 2**31:
            return 0
        if flag:
            return -int(res)
        else:  
            return int(res)

res = Solution.reverse(1,1534236469)
print (res)


