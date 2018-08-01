"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49




"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        #暴力解法
        maxrs = 0
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                maxrs = max(maxrs, (j-i)*(min(height[i],height[j])))
        return maxrs
        """

        """
        面积=底x高，从两边向中间找，所以底会变小，所以如果高度会增大的话，才有比较的意义
        ref:https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation
        """
        if len(height) <= 1:    return 0
        p, q = 0, len(height) - 1
        maxarea =0
        while p < q:
            maxarea = max(maxarea, (q-p)*min(height[p],height[q]))
            if height[p] < height[q]:
                p += 1
            else:
                q -= 1
        return maxarea

so = Solution()

height = [0] #0
height = [1] #0
height = [0,1,0] #0
# height = []
height = [1,8,6,2,5,4,8,3,7]
height = [1,3,2,5,25,24,5]


print(so.maxArea(height))
