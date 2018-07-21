"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]



"""


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """
        这道题与39题的区别是，此题的candidated里面可能有重复的数据，同时，每个数据只能用一次
        所以，可以先排序，然后用set对每个数据出现次数进行统计，每次访问的时候，次数-1.当次数为0的时候，开始下一个
        canset={1:2, 2:1, 5:1, 6:1, 7:1, 10:1}

        额。。。甚至不用这样，直接排完续，[1, 1, 2, 5, 6, 7, 10]    8
        [1, 7],
        [1, 2, 5],
        [2, 6],
        [1, 1, 6]
        第一次： 8-1-1-2-5=<0，停止，并开始进行第二个数字
        第二次： 8-1-2-5=0满足条件，停止，并将路径加入结果


        [1,2,2,2,5]   5

        index=0,path=[].tar=5,rs-[]
            i=0
                dfs(1,[1],4,rs)  -> index=1, path=[1],tar=4, rs=[]
                    i=1
                        dfs(2,[1,2],2,rs) -> index=2.path=[1,2],tar=2,rs=[]
                            i=2
                                dfs(3,[1,2,2],0,rs) -> index=3,path=[1,2,2],tar=0,rs=[]
                                    tar==0 -> rs=[[1,2,2]]开始回溯
                            i=3
                                dfs(4,[1,2,2],0,rs) -> index=4,path=[1,2,2],tar=0,rs=[]
                                    tar==0 所以这里有出现了一个[1,2,2]
                            这两个[1,2,2] 第一个是由下标为 012的三个元素组成的
                                         第二个是由下标为 013的三个元素组成的
                                         因为num[2]和num[3]一样，所以出现了重复的数组，
                                    因此，需要做一些处理，如果target=0时，在传入新的target之前，如果num[i]==num[i+1]的话
                                        下标往后移，所以应该用while
                    i=2
            i=1
            i=2

        [1,2,2,2,2]   5
        index=0,path=[].tar=5,rs-[]
            i=0
                dfs(1,[1],4,rs)  -> index=1, path=[1],tar=4, rs=[]
                    i=1
                        dfs(2,[1,2],2,rs) -> index=2.path=[1,2],tar=2,rs=[]
                            i=2
                                dfs(3,[1,2,2],0,rs) -> index=3,path=[1,2,2],tar=0,rs=[]
                                    tar==0 -> rs=[[1,2,2]]开始回溯
                            i=3
                                dfs(4,[1,2,2],0,rs) -> index=4,path=[1,2,2],tar=0,rs=[]
                                    tar==0 所以这里又出现了一个[1,2,2]
                            这两个[1,2,2] 第一个是由下标为 012的三个元素组成的
                                         第二个是由下标为 013的三个元素组成的
                                         因为num[2]和num[3]一样，所以出现了重复的数组，
                                    因此，需要做一些处理，如果target=0时，在传入新的target之前，如果num[i]==num[i+1]的话
                                        下标往后移，所以应该用while
                    i=2
            i=1
            i=2
        """

        def dfs(index, path, target, rs):
            if target == 0 and  path not in rs:
                rs.append(path)
            else:   
                i = index
                while i < len(candidates):
                    if target < 0:
                        break
                    dfs(i+1, path+[candidates[i]], target-candidates[i], rs)
                    i += 1
        rs = []
        candidates.sort()
        dfs(0, [], target, rs)
        return rs



so = Solution()

candidates = [10,1,2,7,6,1,5]; target = 8
candidates = [2,2,2,1,2]; target = 5;
print(so.combinationSum2(candidates, target))