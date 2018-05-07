"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011 

Example 2:

Input: 128
Output: 1
Explanation: Integer 128 has binary representation 00000000000000000000000010000000

十进制转换为二进制数，然后统计二进制数的1的个数

"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic = {}
        dic[1] = 0
        while n != 0:
            if n%2 == 1:
                dic[1] += 1
            n = int(n/2)
        return dic[1]
so = Solution()

n = 14

rs = so.hammingWeight(n)
print(rs)