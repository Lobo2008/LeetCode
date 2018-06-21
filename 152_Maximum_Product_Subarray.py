"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        找到最大连续相乘的子数组的乘积

        注意，乘法当中，符号具有全局性：正数x正数是正数，会越来越大，负数x负数也是正数。而其他情况都是负数
        因此，需要保留两个数，全局最大值和最小值，如果
        加入rs[n-1]时第x~n-1项的连续乘积，k是数组中第n项的值，
        1）rs[n-1]为正数，k为正数时，rs[n-1]*k是正数，
        2）rs[n-1]为正数，k为负数时，rs[n-1]*k是负数，

        3）rs[n-1]为负数，k为正数时，rs[n-1]*k是负数，
        4）rs[n-1]为负数，k为负数时，rs[n-1]*k是正数，
        乘积最大的，只可能是1和3，其中1时，当然要rs[n-1]是最大正数，3时，rs[n-1]要是最小德负数（此时乘以一个负数才会是最大）
        a>b>0,则乘以一个负数k以后，a<b<0
        反之
        a<b<0,则乘以一个负数k以后,a>b>0


        因此，需要维护一个最大值和一个最小值（虽然最大值和最小值都可能为正或者都为负）


        [2,3,-2,4]
        max=2,min=2,rs=2


        """
        #初始值都是第一个数
        maxVal, minVal, rs = nums[0], nums[0], nums[0]
        for i in range(1,len(nums)):
            """
            如果第n位是负数的话，乘以最值将会翻转，
            因此，此处就将最大值最小值交换，以保证最值不变
            比如 max=3,min=2,nums[i]=-2
            则max*nums[i]=-6
              min*nums[i]=-4
              最大值是-4，最小值是-6，反过来了，所以可以提前变，交换最值
              max=2,min=3,则max*nums[i]=-4,min*nums[i]=-6
            """
            if nums[i] < 0:
                tmp = maxVal
                maxVal = minVal
                minVal = tmp
            maxVal = max(maxVal*nums[i], nums[i])
            minVal = min(minVal*nums[i], nums[i])
            rs = max(maxVal,rs)

            """
            #另一种方法
            #当前项分别和最大值、最小值相乘
            """
            #不管当前是正是负，先乘，然后再比较
            """
            t1 = maxVal*nums[i]
            t2 = minVal*nums[i]
            maxVal = max(max(t1, t2), nums[i])
            minVal = min(min(t1, t2), nums[i])
            rs = max(rs,maxVal)
            """

        return rs

so = Solution()

nums = [2,3,-2,-4]

print(so.maxProduct(nums))
