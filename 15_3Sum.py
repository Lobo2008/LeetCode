"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

先排序，比如
nums = [-4, -1, -1, 0, 1, 2]
通过观察可以知道

和为零的情况（0也算正数）
2个正数+一个负数
1个正数+2个负数

"""
import copy
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        finalres = []
        for i in range(len(nums)-1):      
            for j in range(i+1,len(nums)-1):
                leftnums = copy.deepcopy(nums[j+1:])
                res = []
                if -(nums[i] + nums[j]) in leftnums:
                    res.append(nums[i])
                    res.append(nums[j])
                    res.append(-(nums[i] + nums[j]))
                    if res not in finalres: finalres.append(res)
        return finalres

nums = [-1, 0, 1, 2, -1, -4]
# nums = [-1,0,1]
nums = [0,0,0]
# nums = [14,4,6,-1,10,9,-8,7,-13,14,-13,-11,-8,-9,11,14,-8,-14,-13,7,-10,-15,-13,-11,-11,11,14,13,2,-14,1,-7,-2,14,-1,-15,9,7,-1,3,6,1,7,5,-1,-5,4,-2,-4,-1,-9,-7,-1,-7,-11,3,12,10,-7,-1,12,1,8,-13,1,14,9,-13,6,-7,-3,-11,2,-11,10,-14,-1,-9,0,2,5,6,3,-11,6,7,0,3,3,0,-12,-8,-13,3,-14,-5,2,10,-11,-14,-12,1,-10,5,5,7,-1,11,14,6,-10,-4,-3,8,-7,10,1,8,-1,-11,-15,-6,-12,-13,12,-11]
# nums = [-1,0,1,2,-1,-4]
# nums = [-2,0,1,1,2]
res = Solution.threeSum(1,nums)
print(res)   



"""超时代码  n^2
        nums.sort()
        finalres = []
        for i in range(len(nums)-1):      
            for j in range(i+1,len(nums)-1):
                leftnums = copy.deepcopy(nums[j+1:])
                res = []
                if -(nums[i] + nums[j]) in leftnums:
                    res.append(nums[i])
                    res.append(nums[j])
                    res.append(-(nums[i] + nums[j]))
                    if res not in finalres: finalres.append(res)
        return finalres
"""   