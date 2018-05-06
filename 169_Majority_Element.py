"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

次数大于 n//2的元素
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        times = len(nums)//2
        print('times:',times)
        for index, item in enumerate(nums):
            if item in dic:
                dic[item] += 1
                if dic[item] > times:return item
            else:
                dic[item] = 1
        print(dic)
        return max(dic,key=dic.get)


    """
    分治法
    """
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        a = self.majorityElement(nums[:len(nums)//2])
        b = self.majorityElement(nums[len(nums)//2:])
        if a == b:
            return a
        return [b, a][nums.count(a) > len(nums)//2]


nums = [2,2,1,1,1,2,2]
nums = [2,2,1,1,1,2,2,1]
nums = [8,8,7,7,7]
so = Solution()
rs = so.majorityElement(nums)
print(rs)