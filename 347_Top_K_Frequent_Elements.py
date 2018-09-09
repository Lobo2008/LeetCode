"""
 Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Seen this question in a real interview before?  

"""


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        """
        最简单直接的方法就是遍历一遍，统计出每个元素的个数，然后对次数进行排序，取出前k的元素
        """
        dic = {}
        for ele in nums:
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1
        rs = sorted(dic.items(),key = lambda ele:ele[1],reverse=True)
        rs = [ele[0] for ele  in rs]
        return rs[:k]


so = Solution()

nums = [1,1,1,2,2,3]; k = 2
nums = [];k=0
print(so.topKFrequent(nums, k))