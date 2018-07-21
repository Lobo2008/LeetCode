"""
 Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

"""

class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        """
        这个是求组合的数量，暴力的方法，首先，像39、40一样找出所有和为target的组合，而且这个用过的可以再用，所以每次的i起始值应该是0
        然后，在每个组合中全排列，把不重复的加入结果集，最后求结果集的长度即可
        但是，这样会超时，见 combinationSum4_TLE
        
        ref:https://leetcode.com/problems/combination-sum-iv/discuss/85041/7-liner-in-Python-and-follow-up-question
        i=0
            num=1 break
            num=2 break
            ...
        i=1
            num=1 dp[1]=dp[1]+dp[1-1]=1
            num=2 break
        i=2
            num=1 dp[2]=dp[2]+dp[2-1]=dp[2]+dp[1]=1
            num=2 dp[2]=dp[2]+dp[2-2]=dp[2]+dp[0]=2
            num=3 break
        i=3
            num=1   dp[3]=dp[3]+dp[3-1]=dp[3]+dp[2]=2
            num=2   dp[3]=dp[3]+dp[3-2]=dp[3]+dp[1]=3
            num=3   dp[3]=dp[3]+dp[3-3]=dp[3]+dp[0]=4
            num=4 break

        所以dp[k]就是 和为k的序列的数量
        dp[4]和为4的序列的数量：减去nums[0],也就是1的时候，求dp[4]相当于求dp[3]的数量
       

         #nums=[1,2,3,4]     target= 5    
        注意nums里的元素可以重复使用。

        假设已有序列 [1,1]，和为2，距离target还差 target-2=3的值，这个值可能会是数组里任意一个小于等于3的值
        （1,2、3中的其中一个或者多个）,而3相当于新的target,
            所以现在要求 dp[3]了，而dp[3]是由dp[5减掉“选择”的元素2而来=5-2=3]
        
        然后，比如，选了2,那现在就的组合就是[1,1,2] 距离新target还差 3-2=1的值，这个值可能会是数组里<=1的任意一个数（只有1了）
        所以现在要求dp[1]了，dp[1]是由dp[3减去选择的2而来=3-2=1]

        所以可以看到的是dp[5]=dp[3]+dp[1], 因为省略了很多，所以其实是：dp[5]=dp[4]+dp[3]+dp[2]+dp[1],,,?
            dp[k]=dp[k]+dp[k-选择的某个数]

        """
        nums.sort()
        dp = [1] + [0]* target
        for i in range(target+1):
            for num in nums:
                if num > i:
                    break
                dp[i] = dp[i] + dp[i-num]
        return dp[target]


        
        #超时算法

    def combinationSum4_TLE(self, nums, target):

        def dfs(index, path, target, rs):
            if target == 0:
                rs.append(path)
            else:
                for i in range(len(nums)):
                    if target < nums[i]:
                        break
                    dfs(i, path+[nums[i]], target-nums[i], rs)

        rs = []
        nums.sort()
        dfs(0, [], target, rs)
        return len(rs)
so = Solution()
nums = [1, 2, 3]
nums =[3,2,1,4]
target = 4
print(so.combinationSum4(nums, target))