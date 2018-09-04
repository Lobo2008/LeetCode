"""
 You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:

    The length of the given array is positive and will not exceed 20.
    The sum of elements in the given array will not exceed 1000.
    Your output answer is guaranteed to be fitted in a 32-bit integer.
"""
class Solution:

    
    
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        """数学+dp方法
        nums = {1,2,3,4,5}, target=3, 一种可行的方案是+1-2+3-4+5 =3
        
        也就是 sum({1,3,5}) - sum({2,4}) = target
        拼凑：
            sum({1,3,5}) - sum({2,4}) + sum({1,3,5}) + sum({2,4}) = target + sum({1,3,5}) + sum({2,4})
            # 左边消掉sum{{2,4}}

            2*sum({1,3,5}) =  target + sum(nums)
        ->  sum(P) = (target+sum(all))/2
        此题中 sum(p) = 1+3+5=9
                target = 3
                sum(nums)=1+2+3+4+5=15
            -> 9 = (15+3)/2 bingo

        由于target 和sum(nums)是固定值，所以原始问题转换为了求解nums子集中何为sum(P)的方案的个数

        求解nums中子集合只和为sum(P)的方案个数(nums中所有元素都是非负)可以采用01背包来求解，
        我们初始化dp的长度为(target+sum(nums))/2+1，并且dp[0]=1.递推公式为：
        
        dp[target] =dp[target] + dp[target - nums[i]];

        dp[target]的意思是当累加的和是target时 子集和的个数，那么dp[target]由两部分组成，如果不选择第i个元素，
        那么等于第i-1个元素背包容量为target的子集的和。
        如果选择第i个元素，那么等于第i-1个元素背包容量为target-nums[i]时的子集和个数。

        然后把考虑第i个元素和不考虑第i个元素的情况都加入dp[target]的计算中。还有一点需要注意：
        如果累加和是奇数或者target>sum(nums)，
        那么返回0

        -----
        用dp[target]存储和为target的组合数，然后对nums中的整数nums[i]进行遍历，对于所有target >= nums[i]的
        
        则有dp[target]=dp[target]+dp[target-nums[i]


        假设nums=[1,2,3,4,5],背包为9 kg
         假设目前已经选择了 1和3，那么，当前背包重4kg，还剩5kg，j=5,  dp[j]=0
            (i=2时，选择了重为3kg的东西）
            i=3时来到了4kg的东西：
                                不选4kg，则背包还剩5kg，跟
                                选择以后，背包还剩 、5-4=1kg的东西，即  dp

            i=4时，来到了5kg的东西
                                选择5kg，则背包还剩  5-5=0kg的东西，dp[5]

     
        第一轮，从[1,2,3,4,5]中找和为9的组合数
        第二轮，从[2,3,4,5]中找和为9的组合数
        第三轮,从[3,4,5]中找和为9的组合数
        第四轮，从[4,5]中找和为9的组合数
        第五轮,从[5]中找和为9的组合数

        轮次数=元素数，每开启新的一轮，目标和都为原始的target

    
        """

        if sum(nums) < S or (sum(nums)+S)%2:  return 0
        target = (sum(nums)+S) // 2
        dp = [1]+[0]*target
        nums.sort()
        for i in range(len(nums)):
            x = target
            while x >= nums[i]:
                dp[x] = dp[x] + dp[x-nums[i]]
                x -= 1
        return dp[target]



        
    #dfs的解法 TLE，复杂度2的n次方
    def  findTargetSumWays_dfs(self, nums, S):
    
        def helper(start,nowS):
            if  start >= len(nums):
                if  nowS == 0: 
                    return 1
                return 0 
            count = 0
            count += helper(start+1, nowS-nums[start])
            count += helper(start+1, nowS+nums[start])
            return count
        rs = helper(0,S)
        return rs
    

so = Solution()
nums =[1, 1, 1, 1, 1];  S = 3
# nums = [1,0]; S=1
# nums = [10,9,6,4,19,0,41,30,27,15,14,39,33,7,34,17,24,46,2,46]; S=45 #6606
nums = [1,2,3,4,5]; S=3
print(so.findTargetSumWays(nums, S))