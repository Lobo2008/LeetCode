"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3

"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        """
        类似于word ladder 127，
        遍历每个元素，如果元素g[i][j]是1的话，把他以及他的上下左右都变成0（如果g[i][j]为零，不用浪费时间呐去看周围的元素）
        
        11000
        11000
        00100
        00011

        比如，在处理g[0][0]时，此元素是1，然后把他周围的1全部变为0，得到：(x代表这一步变成了0)
        xx000
        x1000
        00100
        00011
        g[0][0]的右边g[0][1]也是1，将其变成0的同时，发现g[0][1]这个1的下面还有一个1，也就是g[1][1]，所以也“顺便”让他为0
        有一点递归的想法
        """

        def top2btm(i,j):
            if i < 0 or i >= col or j < 0 or j >= row or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            top2btm(i-1, j)#上
            top2btm(i+1, j)#下
            top2btm(i, j-1)#左
            top2btm(i, j+1)#右
        count = 0

        col, row = len(grid),len(grid[0])
        for i in range(col):
            for j in range(row):
                if grid[i][j] == '1':
                    top2btm(i, j)
                    count += 1
        return count


so = Solution()

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]] #1
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]] #3

for item in grid:
    print(item)

print(so.numIslands(grid))
