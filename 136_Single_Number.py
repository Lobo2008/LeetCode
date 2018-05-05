"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Input: [2,2,1]
Output: 1

Input: [4,1,2,1,2]
Output: 4

要求：线性复杂度，不引入额外的存储
思考：https://leetcode.com/problems/single-number/discuss/43000/Python-different-solutions.

1.用数学的方法，set(nums)将获得nums里的值，每个值只获取一次，求和乘以2，再减去原来的和即可
2.也可以用异或的方式，
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)

    """
    下面是一些其他的方法
    """

    """
    遍历nums里的每个值，然后将其作为key存入字典中，每次存入，计数器加一，最后返回val为1的key
    """
    def singleNumber1(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0)+1
        for key, val in dic.items():
            if val == 1:
                return key

    """
    异或的方法 ，nums = [4,1,2,1,2]等于二进制的[100,001,010,001,010]
    1)100时, res = 000^100 = 100(4)
    2)001时, res = 100^001 = 101(5)
    3)010时, res = 101^010 = 111(7)
    4)001时, res = 111^001 = 110(6)
    5)010时, res = 110^010 = 100(4)
    其实可以这么想：nums就是：
        100
        001
        010
        001
        010
      -------
        100(4)
    因为相同的两个数字，异或以后绝对等于000，所以单独的哪一个，就会被“筛选出来”

    """
    def singleNumber2(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res
    
    def singleNumber3(self, nums):
        return 2*sum(set(nums))-sum(nums)
    
    def singleNumber4(self, nums):
        return reduce(lambda x, y: x ^ y, nums)
    
    def singleNumber(self, nums):
        return reduce(operator.xor, nums)   
         
nums = [4,1,2,1,2,5,6,5,6]
nums = [4,1,2,1,2]
so = Solution()
res = so.singleNumber(nums)
print(res)
