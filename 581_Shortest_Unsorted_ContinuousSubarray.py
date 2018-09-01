"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:

Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:

    Then length of the input array is in range [1, 10,000].
    The input array may contain duplicates, so ascending order here means <=.


"""

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        把数组看成折线图，折线图应该是上升或者平行的
        两个指针head 和tail，同时从两边开始，当head指针的路劲下降的时候，找到了start，当tail指针的路径上坡了，找到了end，end-start就是长度

        """

        if len(nums) <= 1:  return 0
        sortnums = sorted(nums)
        head, tail = 0, len(nums)-1
        headFind,  tailFind = False, False
        while head <= tail:
            headRs = nums[head] ^ sortnums[head] == 0
            tailRs = nums[tail] ^ sortnums[tail] == 0
            if not headRs and  not tailRs:   return tail - head + 1
            if headRs:  #等于0的时候要继续比下一个
                head += 1
            if tailRs:  
                tail -= 1
        return 0 

so = Solution()

nums = [2, 6, 4, 8, 10, 9, 15]#5

# nums = [10,9,8,7,6,5]
# nums = []     #0
# nums = [1]    #0
# nums = [1,10] #0
# nums = [10,1] #2
# nums = [2,1,3,4,5]    #2
nums = [2,3,4,5,1]    #5
print(so.findUnsortedSubarray(nums))
