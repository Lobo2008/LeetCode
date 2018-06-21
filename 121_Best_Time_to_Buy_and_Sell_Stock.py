"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        已知股票价格，求买入和卖出后最多能挣的多少钱。
        其实就是最大连续子数组的变体，把价格变成价格差，再求最大子数组和即可

        最大连续子数组和，有三种：在左半边、在右半边、横跨中点
        """
        if not prices:
            return 0
        nums = []
        for i in range(1,len(prices)):
            nums.append(prices[i]-prices[i-1])
        """
        求最大子数组和，用dp方法
        dp[n-1]，x~n-1的最大子数组和，状态方程：
        dp[n]=max(dp[n-1]+nums[i],nums[i])
        """
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1]+nums[i], nums[i])
        #max([])会报错，所以一定要nums not none的时候才能max
        return max(nums) if nums and max(nums) >=0 else 0


so = Solution()

prices = [7,1,5,3,6,4]
print(so.maxProfit(prices))