"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        哈希表的方法，复杂度是O(n)
        """
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target-x in dict:
                return (dict[target-x], i)
            dict[x] = i  #has exchange key=>value to value=>key in dict
        
        
        
        
        """
        也可以先对数组排序，然后利用夹逼的方法，从两边往中间迫近，复杂度是nlogn，不过这种方法需要
        记录原始的index（因为排过序，所以index会变）
        
        ->不对，通不过
        # nums = [3,3];target = 6
        # nums = [3,2,3];target = 6
        """
    def twoSum2(self, nums, target):
        ls = []
        ls[:] = nums[:]
        ls.sort()
        low, high = 0, len(ls) - 1
        while low <= high:
            print(ls[low],' + ',ls[high],' = ',ls[low] + ls[high])
            if ls[low] + ls[high] == target:
                print('~~~1')
                if ls[low] == ls[high]:
                    return [nums.index(ls[low]), nums.index(ls[high]) ] 
                else:
                    return [nums.index(ls[low]), nums.index(ls[high])]

            elif ls[low] + ls[high] > target:
                print('~~~2')
                high -= 1
            else:
                print('~~~3')
                low += 1
        print('~~~4')
        return [nums.index(ls[low]), nums.index(ls[high])]

so = Solution()
nums = [2, 11, 7, 15]; target = 18
#nums =[2,7,11,15]
# nums = [3,3];target = 6
# nums = [3,2,3];target = 6
nums = [-1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 2, 2, 2];target = 4
print(so.twoSum2(nums, target))                   


"""another solution:leetcode.com/problems/two-sum/discuss/17/Here-is-a-Python-solution-in-O(n)-time/363


"""
