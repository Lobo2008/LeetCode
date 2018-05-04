"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
递归调用，对每一个节点进行比较
ref:
    https://leetcode.com/problems/same-tree/discuss/32729/Shortest+simplest-Python
    https://leetcode.com/problems/same-tree/discuss/126574/Easy-to-Understand-Python-Beats-98


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if not p  and not q:
            return True
        if p and q and p.val == q.val:
            x = self.isSameTree(p.left,q.left)
            y = self.isSameTree(p.right,q.right)
            return x and y
        else:return False

p =TreeNode(1)
p.left = 2
p.right = 1

q = TreeNode(1)
q.left = 1
q.right = 2       

so = Solution()
res = so.isSameTree(p,q)
print(res)