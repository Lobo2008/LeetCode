"""

Given a non-empty array containing only positive integers, 
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

    Each of the array element will not exceed 100.
    The array size will not exceed 200.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.


"""

class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        把数组分为两部分，判断一部分的和否等于另一部分的和

        [1,2,3,4,5,11]

        左边和为13，右边和为13，所以可以
        [1,3,4,5]  [11,2]

        数组会分为两部分，两部分的和要相等，于是乎，每部分的和等于 sum(nums) // 2就可以了

        所以问题就变成了，判断两个子数组，每个子数组的和是否为sum(nums)//2，是的话True，反之false

        
        所以其实，这时是一个背包问题：从n个物品中放若干个进入容量为target的书包里，每个物品最多只能用一次，
        是否能够刚好填满书包的重量target
        而这个target = sum(nums)/2

        二维的，好理解：dp[i][j] 从 前i个物品中选，允许的重量/体积/和 为j的时候，所得到的最大的重量/体积/利益/和

            dp[i][j] = dp[i-1][j]                          j < nums[i]的时候
                     = dp[i-1][j] + dp[i-1][j-nums[i]]     j >= nums[i]的时候


        """
        target = sum(nums)
        if target & 1:   return False#和是奇数，说明不可能平分为两半
        target = target >> 1
        nums.sort()
        dp = [True] + [False]*target
        for i in range(len(nums)):
            for j in range(target,-1,-1):
                if j >= nums[i] :   
                    dp[j] = dp[j] or dp[j-nums[i]]
                else:   break
        return dp[target]
        



        
so = Solution()

nums = [1, 5, 11, 5] #true
nums = [1, 2, 3, 5] # false
nums = [1,1]
print(so.canPartition(nums))