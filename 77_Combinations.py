"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]



"""



class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        """ 
        两个数字n和k，找出所有这样的组合：

        1.组合中有k个数字
        2.组合是递增
        3.组合中的数字是{1,2,3,....n} 的子集
        
        比如n=4,k=3的时候     数组为[1,2,3,4]
        用dfs的思想处理，找1开头的 [1,2] [1,2,3][1,2,3]  [1,3][1,3,4] [1,4] 还要把长度不等于k的删除掉
                      找2开头的  [2,3][2,3,4]
                      找3开头的 [3,4]
                    然后把长度不等于k的删除掉
        """

        def dfs(index, path, rs):
            if len(path) == k:
                rs.append(path)
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]], rs)
        rs = []
        
        nums = [i for i in range(1,n+1)]
        dfs(0, [], rs)
        return rs



so = Solution()
n = 4; k = 2
# n = 4; k = 3
print(so.combine(n, k))