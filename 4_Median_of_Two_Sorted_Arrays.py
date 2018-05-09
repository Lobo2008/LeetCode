"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

nums1 = [1, 3]
nums2 = [2]
The median is 2.0

nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5

先归并，然后找到中间的数字，奇数个元素直接取中间值，偶数个元素取中间两个
0123456  有7个元素，中间的是 3 ，就是（len-1）/2
01234567 有8个元素，中间的是34，就是 len/2-1 和len/2

"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                nums.append(nums1[0])
                del nums1[0]
            else:
                nums.append(nums2[0])
                del nums2[0]
        if nums1:nums += nums1
        if nums2:nums += nums2
        l = len(nums)
        if l % 2 == 0:
            return  float(nums[int(l/2-1)]+nums[int(l/2)])/2
        else: 
            return float(nums[int((l-1)/2)])


nums1 = [1, 2, 4 ,5]; nums2 = [3,6,7,8]

nums1 = [1, 3];nums2 = [2]

# nums1 = [1, 2];nums2 = [3, 4]
nums1 = [1,2]; nums2 = [3,4]
res = Solution.findMedianSortedArrays(1,nums1,nums2)

print(res)