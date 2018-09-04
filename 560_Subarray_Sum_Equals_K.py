"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Note:

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].



"""


class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        找到连续和为k的自己的个数
        nums = [4,1,2,3,4,5,6,7,3,3,8] ; k=6
        有三个自己和为6

        [1,2,3]  [6], [3,3]

        找到第一个子集[1,2,3]以后，要从[2,3,4,5...]开始找第2个子集

        3 3 3 3 3 
        4个

 
         nums = [7，6，4,1,2,3,4,5,6,7,3,3,8]
         暴力解法，复杂度是O(n^2)
         而最主要的时间花费在sum(nums[i:j])上面，那么，如果我们事先知道了 sum(nums[0:i]) 和 sum(nums[0:j])的值，
         就可以直接计算sum(nums[i:j])了
         比如例子中  是要计算 sum(nums[3:6]) 即nums[3] + nums[4] + nums[5] == k
         则j = 6,i = 3  sum(nums[3:6])

         按照这个想法，直接遍历一遍，把当前和存到哈希里面即可
        dic = {0:7, 1:13, 2:17, 3:18, 4:20, 5:23, 6:27...}

        当求导 sum = sum + nums[5] = 23时，  sum-k = 23 - 6 = 17，所以要看看字典里有没有17，有的话，计数器加1
        没有的话，把当前的sum存进字典

        key里面存sum的值 is better

        dic={7:1,13:1 ,17:1, 18:1, 20:1, 23:1, 27:1}
        处理到index = 5的时候，sum为23，23-6 = 17，说明sum[0:j]为23，需要找到一个sum[0:i]等于17的

        查字典，发现字典里有一个，所以计数器加1

        如果没有的话，就把当前的sum值最为key存到字典里：
        当index = 6的时候，sum为27，则27-6 = 21，查看需要一个key=21的，但没找到，则sum放入字典

        """
        # nowsum = 0
        # dic = {0:1} #默认下和为0的有一个，就是空集
        # count = 0
        # for i,n in enumerate(nums):
        #     nowsum += n
        #     if nowsum - k in dic:#如果23-6 = 17在dic里的话，计数器+1
        #         count += dic[nowsum - k]
        #     if nowsum in dic: #23+6=29；如果已经有和为23的，说明之前的元素和已经出现一次了，当再次出现和为23的时候，就是两次
        #         dic[nowsum] += 1
        #     else:
        #         dic[nowsum] = 1#如果目前的和23没入库的话，先入一下
        # return count
        
        from collections import Counter
        dic = Counter({0:1})
        count,nowsum = 0, 0
        for i,n in enumerate(nums):
            nowsum += n
            count += dic.get(nowsum - k, 0)
            dic[nowsum] = dic.get(nowsum,0) + 1
        return count



        #简化版
        # sums = {0:1} # prefix sum array
        # res = s = 0
        # for n in nums:
        #     s += n # increment current sum
        #     res += sums.get(s - k, 0) # check if there is a prefix subarray we can take out to reach k
        #     sums[s] = sums.get(s, 0) + 1 # add current sum to sum count
        #     print(sums)
        # return res

so = Solution()
# nums = [9,1,2,3,4,5,6,7,3,3,8] ; k=6
nums = [2,3,2,3,2,3]; k = 5


nums = [3,3,3,3];k = 6
nums = [1,-1,1] ; k = 1
# nums = nums = [7,6,4,1,2,3,4,5,6,7,3,3,8] ; k = 6
print(so.subarraySum(nums, k))