"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42



"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """
        很简单，找出所有子树，然后对每棵子树，找出最大子数组即可
        er....错了，不是单路径，是找子树
        """
        rs, paths = [], []
        if not root:
            return rs
        self.tree_all_path(root, [], rs)
        maxnum = 0
        for item in rs:
            print('tree:',item)
            tmp = self.maxSubArray_DP(item)
            if tmp > maxnum:
                maxnum = tmp
                # rs = item
        return maxnum
    def tree_all_path(self,root, curRs, rs):
        if not root.left and not root.right:
            rs.append(curRs+[root.val])
        if root.left:
            self.tree_all_path(root.left, curRs+[root.val], rs)
        if root.right:
            self.tree_all_path(root.right, curRs+[root.val],rs)

    def maxSubArray_DP(self,nums):

        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        return max(nums)
    # def mainfunc(self,nums):
    #     nums = [-2, 1, -2, 4, 3, 5, 6, 1, 5] 
    #     low,high = 0,len(nums)-1
    #     rs = self.max_subArray_sum(nums,low,high)
    #     return rs

    #  #[-2, 1, -2, 4, 3, 5, 6, 1, 5]  rs=6
    # def max_subArray_sum(self,nums,low,high):
    #     if low == high:
    #         return nums[low]
    #     mid = (low + high ) // 2
    #     left = self.max_subArray_sum(nums,low,mid)
    #     right = self.max_subArray_sum(nums,mid+1,high)
    #     x = self.max_x_subArray_sum(nums,low,high)
    #     return max(left,x,right)
    # def max_x_subArray_sum(self, nums,low,high):
    #     #[-2, 1, -2, 4, 3, 5, 6, 1, 5]  rs=6
    #     leftsum = -10**10
    #     curSum = 0
    #     mid =  (low + high)//2
    #     for i in range(mid,-1,-1):
    #         curSum += nums[i]
    #         if curSum > leftsum:
    #             leftsum = curSum
    #     rightsum = -10**10
    #     curSum = 0
    #     for i in range(mid+1,high,1):
    #         curSum += nums[i]
    #         if curSum > rightsum:
    #             rightsum = curSum
    #     return leftsum+rightsum




so = Solution()

l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
root1 = l1
l1.left = l2; l1.right = l3

t1 = TreeNode(4)
t2 = TreeNode(9)
t3 = TreeNode(0)
t5 = TreeNode(5)
t6 = TreeNode(1)
root2 = t1
t1.left = t2; t1.right = t3
t2.left = t5; t2.right = t6

print(so.maxPathSum(root1))
# print(so.mainfunc(1))