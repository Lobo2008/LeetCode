"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


"""
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
    
        if not matrix:  return []
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        rs = []
        while top < bottom and left < right:
            """
            res.extend(matrix[top][left:right])
            res.extend([matrix[i][right] for i in range(top, bottom)])
            res.extend(matrix[bottom][right:left:-1])
            res.extend([matrix[i][left] for i in range(bottom, top, -1)])

            """
            rs.extend(matrix[top][left:right])
            rs.extend(matrix[i][right] for i in range(top,bottom))
            rs.extend(matrix[bottom][right:left:-1])
            rs.extend(matrix[i][left] for i in range(bottom,top,-1))
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        if top == bottom:
            rs.extend(matrix[top][left:right+1])
        elif left == right:
            rs.extend(matrix[i][left] for i in range(top,bottom+1))
        return rs

        
so = Solution()

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12],
  [13,14,15,16],
  [17,28,19,20],
  [21,22,23,24]
]

matrix = [[2,5,8],[4,0,-1]]
matrix = [[3],[2]]
print(so.spiralOrder(matrix))