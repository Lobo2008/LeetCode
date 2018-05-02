"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"

两个二进制的数字相加，返回二进制的结果

从二进制数的右边往左边看，每一位都要乘以 2的x次方，
x= len(s)-i,是第i为，写一个转换函数即可

十进制转二进制，除以二，余数就是二进制的位，然后反着输出即可

"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        so = Solution()
        adcm = so.binaryToDecimal(a)
        bdcm = so.binaryToDecimal(b)
        res = so.decimalToBinary(adcm+bdcm)
        print(adcm,bdcm,res)
        return  res
    #1011 l = 4
    def binaryToDecimal(self,s):
        l = len(s)
        sum = 0
        for i in range(l-1,-1,-1):
            sum += int(s[i])*(2**(l-1-i))
        return sum
    def decimalToBinary(self,num):
        rs = []
        if num == 0:return str(0)
        while num !=0:
            rs.append(str(num%2))
            num = num //2
        rs.reverse()
        return "".join(rs)
# s = "1011"
# res = Solution.binaryToDecimal(1,s)
a = "1010" ; b = "1011"
a = "0";b="0"

res = Solution.addBinary(1,a,b)
print(res)

num = 11
Solution.decimalToBinary(1,num)