"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
主要的难点在于复杂度，因为是logn，所以可以用二分法

"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums)-1
        mid = int((low+high)/2)
        while low < high:
            if 
    """
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

    Input: nums = [5,6,6,8,8,10], target = 7
    Output: [-1,-1]
    """
    def recurssive(nums,low,mid,high,target):
        print('~~~~~~~~IN')
        if low == high:
            return low
        
        if target < nums[mid]:
            print('~~~~1')
            high = mid
        elif target > nums[mid]:
            print('~~~~2')
            low = mid
        else:
            print('~~~~3')
            return mid
        mid = int((low+high)/2)
        Solution.recurssive(nums,low,mid,high,target)
        
        

nums = [4,5,6,8,8,10]; target = 7
# res = Solution.searchRange(1,nums,target)
low = 0
high = len(nums)-1
mid = int((low+high+1)/2)
res = Solution.recurssive(nums,low,mid,high,target)
print(res)