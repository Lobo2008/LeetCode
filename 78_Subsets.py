"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
          index=0,path=[],rs=[]
            rs=[[]]
            i = 0, dfs(1,[]+[1],[[]])    index=1, path=[1] rs=[[]]
                    rs=[[],[1]]
                    i = 1, dfs(2,[1]+[2],[[],[1]])   index = 2, path=[1,2], rs=[[],[1]]
                           rs=[[],[1],[1,2]]
                           i = 2, dfs(3,[1,2]+[3], [[],[1],[1,2]])   index = 3, path=[1,2,3],rs=[[],[1],[1,2]]
                              rs=[[],[1],[1,2],[1,2,3]]
                              不再进入循环
                          所以此时path=
                    i = 2
                      
            i = 1
            i = 2
        key is :先找从1开始的 1  12 123
              然后找从2开始的 2   23
              再找从3开始的  3 
          ref:https://blog.csdn.net/asd136912/article/details/79572128
        """
        #method 1
        def dfs(nums, index, path, rs):
            rs.append(path)
            for i in range(index, len(nums)):
              dfs(nums, i+1, path+[nums[i]], rs)
        rs = []
        nums.sort()
        path = []
        dfs(nums, 0, path, rs)
        return rs
    """
    初始 rs=[[]]
    num[0]=1,
            []+[1]=[1]  -> rs.append([1])


    """
    def subsets_haha(self, nums):
        rs = [[]]
        for item in nums:
          size = len(rs)
          for j in range(size):
              tmprs = []
              rs.append([item])
              rs.append([rs[j]])
              print(tmprs)
          rs = tmprs
          break

        return rs

so = Solution()

nums = [1, 2, 3]
# print(so.subsets(nums))
print(so.subsets_haha(nums))