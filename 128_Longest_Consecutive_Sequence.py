"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


"""

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """ 
        最直观的做法，就是先排序，然后遍历，记录最大的连续串,复杂度是nlgn
        但是题目已经要求了是O(n),所以不能排序

        例子：[8,2,3,4,5,9,12]
        先统计出现的元素，设置为1
        第一个： 8   找8-1=7是否在字典里并且7没用过 ，不ok，则长度不增加
                    找8+1=9是否在字典里并且9没用过，在，所以长度+1，长度变成2，
                
                因为找到9了，所以继续从9找下去：
                    9-1是否在字典里并且8没用过，注意，因为刚才是从8 过来的，所以过来之前8应该标记为”已处理=>dic[8]=0
                            所以这个不成立，长度不变
                    9+1是否在字典里并且10没用过，不ok，所以长度不变
                    
                注意，找到以后才需要递归再找
            。。。。。所以，以8来找，长度为2

        第二个，2
                找2-1是否在字典里且1没用过，不成立 +0
                找2+1是否在字典里且3没用过，成立 +1，则将2标记为”已处理“，并从3开始再找下去


        """
        def rec(number):

            if not dic[number] or dic[number] == 0: 
                return 0 
            else:
                dic[number] = 0
                count = 1
                count +=rec(number-1)
                count += rec(number+1)
                return count

        if not nums:    return 0

        from collections import Counter
        dic = Counter(nums)
        maxlen = 1
        nowmax = 1
        for n in nums:
            nowmax = rec(n)
            maxlen = max(nowmax,maxlen)
        return maxlen



        # """nlgn
        if not nums:    return 0
        maxlen = 1
        newmax = 1
        nums = list(set(nums))
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                newmax += 1
            else:
                maxlen = max(maxlen,newmax)
                newmax = 1
        return max(maxlen,newmax)

        # """

so = Solution()

nums = [100, 4, 200, 1, 3, 2]
nums = [1,3,5]
nums = [1,2,3,5,7,8,9]
nums = [2,3,4,5,9,12]
print(so.longestConsecutive(nums))