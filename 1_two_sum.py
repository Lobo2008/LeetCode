class Solution(object):
    # @return a tuple, (index1, index2)
    def twoSum(self, nums, target):
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
