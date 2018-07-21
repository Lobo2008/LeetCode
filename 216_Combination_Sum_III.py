"""


Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

    All numbers will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]



"""

class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        """
        给定k，比如k=3，然后在1-9的数字中找到3个数，是这三个数的和为另一个给定的数n，比如n=12
        跟39个40的差不多，区别就在于，39和40中的每条path的长度不限定
        而在此题目中的长度是给定的，同时，所谓的candidated只能是[1-9]中选择
        因此，也比较简单
        """



        def dfs(index, path, target, rs):
            if target == 0:
                if path not in rs:
                    if len(path) == k:
                        rs.append(path)
            else:
                for i in range(index, 10):
                    if target < i:
                        break
                    dfs(i+1, path+[i], target-i, rs)
        rs = []
        dfs(1, [], n, rs)
        return rs

so = Solution()
k = 3; n = 12
print(so.combinationSum3(k, n))
