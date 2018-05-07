"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]



Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
"""

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """


        for i in range(k%len(nums)):
            tmp = nums.pop()
            nums.insert(0,tmp)
        print(nums)
    """
    The previous one can truly change the value of old nums, 
    but the following one just changes its reference to a new nums not the value of old nums.
    
    从最后一位竖起，往前推k位，最为新数组的第一部分
    从第一位开始，到底k位，作为数组的第二部分
    合并即可，必须要用nums[:]
    """ 
    def rotate2(self, nums, k):
        l = len(nums)
        k = k % l
        nums[:] = nums[l-k:] + nums[:l-k] #这里必须是nums[:]而不是nums,因为nums只改变形参

so = Solution()

nums = [1,2,3,4,5,6,7] ;k = 8

# nums = [1,2,3] ;k = 2

rs = so.rotate(nums,k)