"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        """ 
        又是数组，应该是回溯+dfs
        遍历每行每列，当找到一个1的时候，开始递归查找这个1右边和边的元素（因为遍历是从左往右从上往下的，所以不用再找左边和下边）




        假设是这样，然后i=1,j=1，即处理到了x元素
        1 1
        1 x
        此时，如果x元素是0，进行下一个判断
            如果x元素是1，则此时的的正方形由x的左边[i][j-1],上边[i-1][j],左上边[i-1][j-1]决定，
            如果这三个元素中有一个为0，则当前的最大面积只为1，即x元素本身
            如果这三个元素都为1的时候，元素才是2，所以，此时dp[i][j] 等于2，
            当判断到i=3,j=3的时候，也是一样的

        """

        if len(matrix) == 0 or len(matrix[0]) == 0: return 0
        h, w = len(matrix), len(matrix[0])
        dp = [[0]*(w+1) for i in range(h+1)]
        rs = 0
        for i in range(1,h+1):
            for j in range(1,w+1):
                if matrix[i-1][j-1] == '0': continue
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
                rs = max(rs, dp[i][j]**2)
        return rs 

    """
        1 0 1 0 0
        1 0 1 1 1
        1 1 1 1 1
        1 0 0 1 0

        Output: 4
    """




so = Solution()

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
for item in matrix:
    print(item)

print(so.maximalSquare(matrix))
