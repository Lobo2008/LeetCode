class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target-x in dict:
                return (dict[target-x], i)
            dict[x] = i  #has exchange key=>value to value=>key in dict

nums = [2, 11, 7, 15]
#nums =[2,7,11,15]
target = 9
print (nums)
res = Solution.twoSum(1, nums, target)                   
print (res)

"""another solution:leetcode.com/problems/two-sum/discuss/17/Here-is-a-Python-solution-in-O(n)-time/363

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i

"""