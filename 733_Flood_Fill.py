"""
 An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:

Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

Note:
The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

"""
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        """ 
        [1, 1, 1]
        [1, 1, 0]
        [1, 0, 1]
        给定坐标(sr,sc) 如 (1,1)
        将这个值和与这个坐标相邻且值相等的点涂成 newColor的值，递归涂
        第一次
        [1, 2, 1]
        [2, 2, 0]
        [1, 0, 1]
        随后
        [2, 2, 2]
        [2, 2, 0]
        [2, 0, 1]

        dfs
        """
        def dfs(image, i, j):
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != oldColor:
                return False
            image[i][j] = newColor
            dfs(image, i+1, j)
            dfs(image, i-1, j)
            dfs(image, i, j+1)
            dfs(image, i, j-1)


        if len(image) == 0 or len(image[0]) == 0:   return []
        oldColor = image[sr][sc]
        if oldColor != newColor:
            dfs(image, sr, sc)
        return image

        

so = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]];sr = 1; sc = 1; newColor = 2
image = [[0,0,0],[0,1,1]]; sr = 1;sc = 1; newColor = 1
print('----before----')
for item in image:
    print(item)
rs = so.floodFill(image, sr, sc, newColor)
print(rs)
print('----after----')
for item in rs:
    print(item)



