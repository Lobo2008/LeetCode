"""

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(index, path, rs):
          if path not in rs:
            rs.append(path)
          for i in range(index, len(nums)):
            dfs(i+1, path+[nums[i]], rs)
        rs = []
        nums.sort()
        path = []
        dfs(0, path, rs)
        return rs

so = Solution()

nums = [1, 2, 2]

print(so.subsetsWithDup(nums))