"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.


Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6,7],       n = 4

Output: [1,2,2,3,5,6,7]

插入排序？归并排序？但是有要求：不能反悔任何数据，而是把nums1改了
m和n不是list的长度，而是list；里非零元素的个数
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2
        nums1.sort()
        """
        index = 0
        while nums2:
            if nums1[index] == 0:
                nums1[index] = nums2[0]
                del nums2[0]
            elif nums2[0] < nums1[index]:
                tmp = nums1[index]
                nums1[index] = nums2[0]
                nums2[0] = tmp
                nums2 = sorted(nums2)
            index +=1   
        print('res',nums1,nums2)
        """






nums1 = [1,2,3,5,7,9,0,0,0,0,0]; m = 6
nums1 = [0];m =0
nums2 = [2,4,6,8];n = 4

nums1 = [1,2,3,0,0,0,0,0]
nums2 = [2,5,6]

nums1 = [-1,0,0,3,3,3,0,0,0]

nums2 = [1,2,2]


so = Solution()
res = so.merge(nums1, m, nums2,n)
# print(res)