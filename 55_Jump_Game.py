"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

【2，3，1，0，4】
"""
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
            [2,3,1,0,4]
            倒过来看，4的下标是4，要到达4，则往前一个,下标为3的值至少是1->no,往前两个,下标为2的值至少为2->no,往前三个,下标为1的值至少为3-> yes
                    此时，要到达的地方变成了下标为2的地方（值为3）

        4的下标是  target=len(nums)-1
                往前一个 下标为 target-1，值至少是1
                往前两个 下标为 target-2，值至少是2
                ...
                往前k个  下标为 target-k，值至少是k ，满足要求时，可将新的目标设为这个k所在的位置
                条件是 target-k >=0
        """
        if len(nums) <= 1:  return True
        targetIndex = len(nums) - 1
        k = 1
        while targetIndex - k >= 0:
            pre = targetIndex - k
            if nums[pre] >= k:
                if pre == 0: #到达第0个元素了
                    return True
                targetIndex = pre
                k = 1
                continue
            k += 1
        return False
        #[3,2,1,0,4]

        #a better/faster solution
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal


so = Solution()

nums = [2,3,1,0,4] #true
nums = [2,3,1,1,4] #true 
# nums = [3,2,1,0,4] #false
nums = [10,0,0,0,0,2]
nums = [0]
print(so.canJump(nums))