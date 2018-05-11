"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false


1.因为matrix的性质，所以其实可以把二维数组合并为一维数组，然后bs就可以了
# 2.target和每一维的第一个元素进行比较，如果target > matrix[x][0]，那如果target存在，则必定在

"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ls = []
        for i in range(len(matrix)):
            ls += matrix[i]
        print(ls)
        if not matrix:return False
        low, high = 0, len(ls)-1
        while low <= high:
            mid = (low + high) // 2
            if ls[mid] == target:
                return True
            elif ls[mid] < target:
                low = mid + 1
            else:
                high = mid - 1    
        return False
so = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 523
print(so.searchMatrix(matrix, target))