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

        ref:https://blog.csdn.net/u014251967/article/details/53611247

        index=0, path=[],rs=[],tar=8
            i = 0
                dfs(0,[2],[],6)     -> index=0,path=[2],rs=[],ta=6
                    i = 0
                        dfs(0,[2,2],[],4)   -> index=0,path=[2,2] rs=[] ,tar = 4
                            i=0
                                dfs(0,[2,2,2],[],2) -> index=0,path=[2,2,2], tar=2
                                    i=0 
                                        dfs(0,[2,2,2,2],rs,0)   ->index=0,path=[2,2,2,2],rs=[],tar=0
                                            tar==0 -> rs=[2,2,2,2] return开始回溯
                                    i = 1
                                        dfs(1,[2,2,2,3],rs,-1)  -> index=0,path=[2,2,2,3] tar=-1
                                            tar <0,stop 再回溯
                            i= 1
                                dfs(1,[2,2,3])...
        
        注意终止条件，8-2-2-2-2=0 的时候，满足情况，终止并将路劲加入
                    8-2-2-2-3=-1的时候，也应该终止，并回到上一次的地方

        """
        def dfs(index, path, rs, target):
            if target == 0:#如果target刚好减到0，则能构成一个路径
                rs.append(path)
            else:
                for i in range(index, len(candidates)):
                    if target < 0:
                        break
                    #注意这里的第一个参数是 ，而不是i+1,因为可以重复使用，所以一直减同一个数
                    dfs(i, path+[candidates[i]], rs, target - candidates[i])

        rs = []
        dfs(0, [], rs, target)
        return rs


so = Solution()

candidates = [2,3,5]; target = 8
# candidates = [1,2,3,6] ; target = 6
print(so.combinationSum(candidates, target))