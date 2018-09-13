"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:

You can assume that you can always reach the last index.


"""

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        The main idea is based on greedy. Let's say the range of the current jump is [curBegin, curEnd], 
        curFarthest is the farthest point that all points in [curBegin, curEnd] can reach. 
        Once the current point reaches curEnd, then trigger another jump, and set the new curEnd with curFarthest, 
        then keep the above steps, as the following:
        ref:    https://leetcode.com/problems/jump-game-ii/discuss/18014/Concise-O(n)-one-loop-JAVA-solution-based-on-Greedy

        """
        # path = []
        curEnd = rs = curFar = 0
        for i in range(len(nums)-1):
            curFar = max(curFar, i+nums[i])
            # if path is needed
            # if i + nums[i] > curFar:
            #     path.append(i)
            #     curFar = i + nums[i]
            if i == curEnd:
                rs += 1
                curEnd = curFar
        return rs



so = Solution()

nums = [2,3,1,1,4]
# nums = [0,1]
print(so.jump(nums))
