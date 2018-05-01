"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

Given nums = [0,0,1,1,1,2,2,3,3,4],

[0,0,0,1,1,1,2,2,3,3,4],
[0,1,1,1,2,2,3,3,4],
[0,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.

因为是sorted的，所以有重复的删掉即可
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 1
        while start < end and end < len(nums):
            if nums[start] == nums[end]:
                nums.remove(nums[end])
                # start += 1
            else:
                start += 1
                end +=1
        return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2]
nums = [0,0,0,0,0]
res = Solution.removeDuplicates(1,nums)
print(res)