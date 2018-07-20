"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

"""
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """
        有点像ksum?

        Input: candidates = [2,3,5], target = 8,
        A solution set is:
        [       
            [2,2,2,2],
            [2,3,3],
            [3,5]
        ]

        i = 2时，tmprs=[]
                8-2=6 ,not in num[i:], rs=[2] ,     6 > i
                6-2=4, not in num[i:], rs=[2,2]     4 > i
                4-2=2, in  num[i:] rs=[2,2,2,2]        break
                rs=[[2,2,2,2]]

        i = 3时，tmprs=[]
                8-3 = 5 in num[i:], rs=[3,5] brea
                rs=[[2,2,2,2],[3,5]]
        i = 5时,tmps=[]
                8-5 = 3 not in num[i:] 3 > i不成立 break


        8-2-2-2-2 = 0 ok
         
        8-3-3-3=-1 x


        Input: candidates = [2,3,6,7], target = 7,
        A solution set is:
        [
            [7],
            [2,2,3]
        i=2时
            7-2 = 5 not in nums[i:] 且 5 > i  tmprs=[2]
            5-2 = 3 in nums[i],break          tmps[2,2,3]
        i = 3时
            7-3 = 4 no in 且4 > i
            4-3 = 1 not in 且 1 > i不成立，返回[]

        可知当 leftnum not in nums[i]且 leftnum > i 的时候回继续减下去
        知道

        2 3 6 12    12 

        """
        def dfs(index, path, rs):
            lssum = 0
            for item in path:
                lssum += item
            if path not in rs and lssum == target:
                rs.append(path)
            for i in range(index, len(candidates)):
                dfs(i+1,path+[candidates[i]], rs)
        rs = []
        dfs(0, [], rs)
        return rs


so = Solution()

candidates = [2,3,5]; target = 8
print(so.combinationSum(candidates, target))