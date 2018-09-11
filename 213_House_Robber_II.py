"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.

Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        比第一代多了一个条件，那就是，rob了第一个house以后不能rob最后一个house
        [1,2,3,1]
        所以其实可以这样？
        如果rob了第一个，则nums其实是 [1,2,3]
            否则，就是 [2,3,1]
        """
        if not nums:    return 0
        if len(nums) <= 3: return max(nums)
        dp1 = [nums[0],nums[1]]+[0]*(len(nums)-3)
        dp2 = [nums[1],nums[2]]+[0]*(len(nums)-3)    
        """
        [6,6,4,8,4,3,3,10]

        nums1 =  [6,6,4,8,4,3,3]
        nums2 =    [6,4,8,4,3,3,10]
        l = 7
        所以i = 2 3 4 5 6

        i=2时   
                max(dp1[i-1])+nums1[2]  => max(dp1[:i-1])+nums[2]
                在i=len-1时，dp1应该停止

                max(dp2[i-1])+nums2[2]  => max(dp2[:i-1])+nums[3]
        i = 3时...
        ...
        i=5时
                max(dp1[i-1])+nums1[5]  => max(dp1[:i-1])+nums[5]

                max(dp2[i-1])+nums2[5]  => max(dp2[:i-1])+nums[6]
        i=6时
                max(dp1[i-1])+nums1[6]  => max(dp1[:i-1])+nums[6]
                max(dp2[i-1])+nums2[6]  => max(dp2[:i-1])+nums[7]
        """
        for i in range(2,len(nums)-1):
            dp1[i] = max(dp1[:i-1])+nums[i]
            dp2[i] = max(dp2[:i-1])+nums[i+1]
        return max(max(dp1),max(dp2))






so = Solution()
nums = [1,2,3,1]
# nums = [6,6,4,8,4,3,3,10] # 27
print(so.rob(nums))



        # method of robber I
        # dp,nothing to say
        if not nums:    return 0
        if len(nums) <= 2: return max(nums)
        dp = [nums[0],nums[1]]+[0]*(len(nums)-2)
        for i in range(2,len(nums)):
            dp[i] = max(dp[:i-1])+nums[i]
        return max(dp)

        #using nums = [6,6,4,8,4,3,3,10] as exaple

        # method of 1.39%
        # here , we can divide nums into nums1 and nums2,then 
        # respectively implementing the Robber I method on nums1 and nums1
        # nums1 = [6,6,4,8,4,3,3] ->   max is 17
        # nums2 = [6,4,8,4,3,3,10] -> max is 27
        # thus the final result is 27
        if not nums:    return 0
        if len(nums) <= 3: return max(nums)
        nums1, nums2 =[], []
        nums1[:] = nums[:len(nums)-1]
        nums2[:] = nums[1:]

        dp1 = [nums1[0],nums1[1]]+[0]*(len(nums1)-2)
        dp2 = [nums2[0],nums2[1]]+[0]*(len(nums2)-2)
        
        for i in range(2,len(nums1)):
            dp1[i] = max(dp1[:i-1])+nums1[i]
        for j in range(2,len(nums2)):
            dp2[j] = max(dp2[:j-1])+nums2[j]
        return max(max(dp1),max(dp2))

        

        # method of 13.6%
        # in method of 1.39%, we(I) NAIVELY using twice FOR X IN RANGE(xxx)
        # but actually, we can reduce to once

        if not nums:    return 0
        if len(nums) <= 3: return max(nums)
        nums1, nums2 =[], []
        nums1[:] = nums[:len(nums)-1]
        nums2[:] = nums[1:]

        dp1 = [nums1[0],nums1[1]]+[0]*(len(nums1)-2)
        dp2 = [nums2[0],nums2[1]]+[0]*(len(nums2)-2)
        
        for i in range(2,len(nums1)):
            dp1[i] = max(dp1[:i-1])+nums1[i]
            dp2[i] = max(dp2[:i-1])+nums2[i]
        return max(max(dp1),max(dp2))



        # method of 98.1%
        # in method of 13.6% and formmer, we used extra space nums1 and nums2
        # but actually, using nums itself is enough
        # attention,  nums2[i+1] = nums[i] ,so replace  nums2 by nums
        #           and, the length of the loop is len(nums)-1,not len(nums)
        if not nums:    return 0
        if len(nums) <= 3: return max(nums)
        dp1 = [nums[0],nums[1]]+[0]*(len(nums)-3)
        dp2 = [nums[1],nums[2]]+[0]*(len(nums)-3)    
        for i in range(2,len(nums)-1):
            dp1[i] = max(dp1[:i-1])+nums[i]
            dp2[i] = max(dp2[:i-1])+nums[i+1]
        return max(max(dp1),max(dp2))
