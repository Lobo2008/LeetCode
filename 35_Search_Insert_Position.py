"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Input: [1,3,5,6], 5
Output: 2

Input: [1,3,5,6], 7
Output: 4

Input: [1,3,5,6], 0
Output: 0

Input: [1,3,5,6], 7
Output: 4

12346789   5
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index in range(len(nums)):
            if target <= nums[index]:
                return index
        return len(nums)
            
nums = [1,3,5,6]; target = 5

res = Solution.searchInsert(1,nums,target)
print(res)