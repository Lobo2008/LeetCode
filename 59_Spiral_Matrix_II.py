"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

4:


[[1, 2 ,3,4],
[12,13,14,5],
[11,16,15,6],
[10, 9, 8,7]
]

"""
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        top, bottom = 0, n-1
        left,right = 0, n-1
        k = 0
        rs = [[0 for i in range(n)] for j in range(n)]
        while top <= bottom and left <= right:
            for i in range(left,right+1):
                k += 1
                rs[top][i] = k
            top += 1
            for i in range(top,bottom+1):
                k += 1
                rs[i][right] = k
            right -= 1
            for i in range(right,left-1,-1):
                if top <= bottom:
                    k += 1
                    rs[bottom][i] = k
            bottom -= 1
            for i in range(bottom,top-1,-1):
                if left <= right:
                    k += 1
                    rs[i][left] = k
            left += 1
        return rs
















        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            print(i,j,di,dj,k+1)
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                print('---in')
                di, dj = dj, -di
            i += di
            j += dj
        return A
        

so = Solution()

n = 4
print(so.generateMatrix(n))