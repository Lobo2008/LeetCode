"""
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

Example 1:

Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}

Note:

    N is an integer within the range [1, 20,000].
    The elements of A are all distinct.
    Each element of A is an integer within the range [0, N-1].


"""

class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        从多个起点到达同一个值之后的路径都是完全相同的，所以每个值最多遍历一次，时间复杂度O(N)，每次遍历到就加到set中
        [5,4,0,3,1,6,2]
        ref:https://blog.csdn.net/fuxuemingzhu/article/details/79460546
        """

        visited = [False]*len(nums)
        maxlen = 0
        for i in range(len(nums)):
            nowmax = 0
            while  visited[i] == False :
                nowmax += 1
                visited[i] = True
                i = nums[i]
            maxlen = max(maxlen,nowmax)
        return maxlen

so = Solution()

nums =  [5,4,0,3,1,6,2]
nums = []
print(so.arrayNesting(nums))