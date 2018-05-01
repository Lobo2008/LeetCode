"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.


Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.


Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.

"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        num = 0
        for index in range(len(nums)):
            if val == int(nums[index]):
                num += 1
        
        for index in range(num):
            nums.remove(val)
        return len(nums)   


# test_case ={"3":[3,2,2,3], "5":[0,1,2,2,3,0,4,2]}

nums = [3,2,2,3] ;val = 3  # [2, 2]
nums = [0,1,2,2,3,0,4,2]; val = 2   #

res = Solution.removeElement(1,nums, val)
print (res)