"""

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:

Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:

Input: [1,2,2,3,1,4,2]
Output: 6

Note:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

"""


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:    return 0
        from collections import Counter
        numsC =  Counter(nums).most_common()
        most = []
        for item in numsC:
            if item[1] != numsC[0][1]: break
            most.append(item[0])      
                  
        minlen = len(nums)
        for i in range(len(most)):
            minlen = min(minlen,(len(nums)-1-nums[::-1].index(most[i]) - nums.index(most[i]) +1) )
            # end = len(nums)-1-nums[::-1].index(most[i])
            # start = nums.index(most[i])
            # l = end - start + 1
            # minlen = min(minlen,l)
        return minlen

        
so = Solution()

nums = [11, 22, 12, 13, 11, 11, 13, 13]
# nums = [1,2,2,3,1]
# nums = [1,2,2,3,1,4,2]
# nums = []
print(so.findShortestSubArray(nums))