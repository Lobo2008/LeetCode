"""
 You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:

Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:

Given nums1 = [1,2], nums2 = [3],  k = 3 

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]



"""


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        if not nums1 or not nums2 or k <= 0:    return []
        rs =[]
        h = []

        for i in range(len(nums1)):
            heapq.heappush(h,(nums1[i]+nums2[0],i,0))
        while h and k > 0:
            print(h)
            small, i, j = heapq.heappop(h)
            # print(i,j)
            rs.append([nums1[i],nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(h,(nums1[i]+nums2[j+1],i,j+1))
            k -= 1
        return rs

        # if not nums1 or not nums2 or k <= 0:    return []
        # rs =[]
        # nums = [[[i,nums2[0]],i+nums2[0]] for i in nums1]
        # i = 1
        # j = 0
        # while len(rs) < k and i < len(nums2):
        #     print('------',nums)
        #     while j < len(nums1)  :
        #         print(j,i,'=>',nums)
        #         tmp,_ = nums.pop(0)
        #         rs.append(tmp) 
        #         tmprs = [nums1[j],nums2[i]]
        #         add = [tmprs,sum(tmprs)]
        #         print('     pop',tmp,', add:',add)
        #         nums.append(add)
        #         nums = sorted(nums, key=lambda ele:ele[1])            
        #         j += 1
        #     i += 1
        #     j = 0
        # leftnum = k-len(rs)
        # leftpart = [i[0] for i in nums[:leftnum]]
        # if len(rs) < k:rs.extend(leftpart) 
        # return rs

so = Solution()
# nums1 = [1,7,11]; nums2 = [2,4,6];  k = 3
nums1 = [2,9,10,15]; nums2 = [1,7,11,16]; k = 5
# nums1 = [2,9,10,15];nums2 = [1];k = 6
# nums1 = [2]; nums2 = [1,7,11,16]; k = 5
nums1 = [1,1,2];nums2 = [1,2,3];k=10
# nums1 = [1,2,3];nums2=[4,5,6];k=10
nums1 = [0,0,0,0,0];nums2 =[-3,22,35,56,76];k=100

nums1 = [1,7,11];nums2 = [2,4,6];k=14

print(so.kSmallestPairs(nums1, nums2, k))