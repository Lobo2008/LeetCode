"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

可以用分治法：
    最大和，是三种情况之一：
        左边、右边、左中右  然后取最大值

坑：下标不用返回，直接返回最大值即可（不明白为什么很多方法都返回了始末的下标）

"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1 
        mid = (low+high+1)//2 
        so = Solution()
        res = so.findMaxSubSum(nums,low,high)
        return res

    """
    找出跨越重点的最大值   
    复杂度为O(n)
    """
    def finaMaxCrossSum(self,nums, low, mid, high):
        leftMaxSum = -10**10
        leftSum = 0
        for  i in range(mid,low-1,-1):
            leftSum += nums[i]
            if leftSum > leftMaxSum:
                leftMaxSum = leftSum
        rightMaxSum = -10**10
        rightSum = 0
        for j in range(mid+1,high+1,1):
            rightSum += nums[j]
            if rightSum > rightMaxSum:
                rightMaxSum = rightSum
        return leftMaxSum+rightMaxSum

    """
    left和right部分，都是T(n)=T(n/2)，所以复杂度为O(lgn)
    而crossing部分为n,所以总的复杂度为   O(nlgn)
    """
    def findMaxSubSum(self,nums, low, high):
        if low == high:
            return nums[low]
        mid = (low + high)//2
        l_sum  = self.findMaxSubSum(nums,low,mid)
        r_sum = self.findMaxSubSum(nums,mid+1,high)
        x_sum = self.finaMaxCrossSum(nums,low,mid,high)
        return max(l_sum,x_sum,r_sum)

    """
    动态规划解法:

    rs[n-1]是前n-1个数的最大的和，k是第n项的值
    比如[ 1, -3, 4, -1, 2, 1, -5, 4]   下标从0开始

    rs[1]=-2，因为前2项的最大和是 1+(-3)=-2
    rs[2]=? , 需要考虑1,-3,4
        前两项的最大和是第0项+第1项，等于-3
        再加一个4，等于1
        但是，第3项，num[2]=4是大于1的，所以前3箱的最大和，用第3项到第3项的和代替就可以了，也就是4

        所以，关系式是：
            dp[n]=  dp[n-1]+nums[n]  
                    nums[n]

    [-2, 1, -3, 4, -1, 2, 1, -5, 4]


    """
    def maxSubArray_DP(self,nums):

        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        print(nums)
        return max(nums)


so = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4] #9
# nums=[-3,100,-1]
# nums = [-1,-2,-3,100]
# nums = [1, -2, 3, 10, -4, 7, 2, -5]
# nums = [0,-2,0] # 0
# low = 0
# high = len(nums)-1 
# mid = (low+high+1)//2 #4.5->4
# res = Solution.findMaxSubSum(nums,low,high)
# res = Solution.MaxCrossSubArray(nums,low,mid,high)

# print(res)
# a=nums
# res = (Solution.MaxSubArray(a,0,len(a)-1))

print('~~~~~ori:',nums)
# res =Solution.maxSubArray(1,nums)
print(so.maxSubArray_DP(nums))


