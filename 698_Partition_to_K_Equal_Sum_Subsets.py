"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Note:
1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""

class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        """
        有重复元素，每个元素都要用到，并且只能用一次

        sum(nums) = 20 , 20/k = 5，所以题目变成了
        找到子集和为target的数目，并且个子集求并集是全集，求交集是空集

        target = sum(nums)/k

        首先 sum(nums)/k必须要除尽，不然是不存在这种组合的
        """
        target = sum(nums)
        if target % k:  return False
        target  = target // k
        # target // = k
        nums.sort()
        

so = Solution()

nums = [4, 3, 2, 3, 5, 2, 1]; k = 4