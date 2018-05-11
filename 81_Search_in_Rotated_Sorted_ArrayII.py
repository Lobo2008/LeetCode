"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:

    This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
    Would this affect the run-time complexity? How and why?


"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:return False
        ls = [i for i in set(nums)]
        ls.sort()
        print(ls)
        low, high = 0, len(ls) - 1
        while low <= high:
            mid = (low + high) // 2
            if ls[mid] == target:
                return True
            elif ls[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False




so = Solution()
nums = [2,5,6,0,0,1,2]; target = 0
nums = [2,2,2,0,1];target = 0
# nums = [2,5,6,0,0,1,2]; target=6
# nums = [2,2,0,2,2,2] ;target = 
nums = [1,3];target = 2
# nums = [1,3,1,1,1] ; target = 3
nums = [10,10,10,-10,-10,-10,-10,-9,-9,-9,-9,-9,-9,-9,-8,-8,-8,-8,-8,-8,-8,-8,-7,-7,-7,-7,-6,-6,-6,-5,-5,-5,-4,-4,-4,-4,-3,-3,-2,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,2,2,2,3,3,3,4,4,4,5,5,5,5,6,6,6,7,7,7,7,7,8,8,8,8,9,9,9,9,9,9,9,10,10]
target = -6
print(so.search(nums, target))