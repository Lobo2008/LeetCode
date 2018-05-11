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
            


    def searchInsert_binary_search(self, nums, target):
        low = 0
        high = len(nums)
        if target > nums[high-1]:return high
        while low <= high:
            mid = (low + high) // 2
            # print('low=',low,',mid=',mid,',high=',high)
            if target == nums[mid] :
                # print('~~~~1')
                return mid
            elif target > nums[mid]  :
                # print('~~~~2')
                low = mid + 1
                index = mid + 1 
                flag =  'right'
            else:# target < nums[mid] 
                # print('~~~~3')
                high = mid - 1
                index = mid  - 1
                flag = 'left'
        # print(low,mid,high,'->',flag)
        return low



so = Solution()
nums = [1,3,5,6,7,9]; target = 3


# print(so.searchInsert_binary_search(nums,target))

for i in range(0,11):
    rs = so.searchInsert_binary_search(nums,i)
    print(i,'=>',rs)