"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]



[-5, -4, -1, -1, 0, 1, 1, 2, 4, 5, 8, 10, 10] target = 15

a + b + c + d = target
在3sum的基础上进行扩展？

    先排序
    先固定一个数，比如-5，
        然后在[-4, -1, -1, 0, 1, 1, 2, 4, 5, 8, 10, 10] 中找到三个数和为 target -(-5)=20的组合
        这部分就属于3sum了，很简单？

"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """
        3sum，在nums[low:]中找到和为target的三个数组合
        """
        nums.sort()
        print('~~~~4sum ori:',nums)
        rs = []
        i = 0
        while i < (len(nums)-3):
            a = nums[i] 
            newTarget = target - a
            print('固定',a,'，在',nums[i+1:],'中找和为',newTarget,'的3个数')
            if i >= 1 and nums[i] == nums[i-1]:
                while i < (len(nums) - 3) and nums[i] == nums[i-1]:
                    i += 1
                continue
            tmpRs = self.threeSum(nums,i+1,newTarget)
            print('   rs=',tmpRs)
            for sum3 in tmpRs:
                sum3 += [a]
                sum3.sort()
                rs.append(sum3)
            i += 1
        return rs
        
    def threeSum(self, nums, low, target):
        # nums = [-1, 0, 1, 2, -1, -4,-1,-1,-1,-1,-1,2,2,3]; target = 5 #1 2 2 
        # nums = [-4, -1, -1, -1, 0, 1, 2, 2, 2, 3,1,2,2]
        # nums.sort()
        # low = 0
        print('  -----3sum ori:',nums)
        pos = list(set([i for i in nums[low:] if i > 0]))
        neg = list(set([i for i in nums[low:] if i < 0]))
        dic = {}

        for i in nums[low:]:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        # print(pos)
        # print(neg)
        # print(dic)
        rs = []
        for i in range(low,len(nums)-2):
            a = nums[i]#fix
            newTarget = target - a # 5-1=4
            l, r = i+1, len(nums)-1
            
            print('  固定',a,'，在',nums[l:r+1],'中找和为',newTarget,'的两个数')
            if i > low and nums[i] == nums[i-1]:
                while i > low and i < len(nums) - 2 and nums[i] == nums[i-1]:
                    i += 1
                # print('应当跳过')
                continue
            while l < r:
                # print(nums[l],'+',nums[r],'=',nums[l],'+',nums[r],' VS ',newTarget)
                if nums[l] + nums[r] == newTarget: # 2+2=4
                    tmp = [nums[l],nums[r],a]
                    tmp.sort()
                    rs.append(tmp)
                    print('    --> found ',tmp)
                    l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r+1] and r > (low + 2):
                        r -= 1
                    while l < r and nums[l] ==  nums[l-1] and r < len(nums)-2:
                        l += 1
                elif nums[l] + nums[r] > newTarget:
                    # print(nums[l] + nums[r],'比',newTarget,'大','  <--')
                    r -= 1
                    # while l < r and nums[r] == nums[r+1] and r > (low + 2):
                        # r -= 1

                else:
                    # print(nums[l] + nums[r],'比',newTarget,'小','  -->')
                    l += 1
                    # while l < r and nums[l] ==  nums[l-1] and r < len(nums)-2:
                        # l += 1
        return rs




so = Solution()
nums = [-1, 2, 1, -4]; target = 1
nums = [-5,-4, -1, -1, 0,1, 1,2,4,5,8,10,10] ;target = 15  #[[-5,0,10,10],[-5,2,8,10],[-4,-1,10,10],[-4,1,8,10],[-4,4,5,10],[-1,1,5,10],[-1,2,4,10],[0,1,4,10],[0,2,5,8],[1,1,5,8],[1,2,4,8]]
# nums = [1,1,1,1,1,1,1,1]; target=0
print(so.fourSum(nums, target))
# print(so.threeSum(nums,1, target))
