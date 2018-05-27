"""
给定一颗二叉树，输出所有的路径：
    4
   / \
  9   0
 / \
5   1

输出：[[4, 9, 5], [4, 9, 1], [4, 0]]
此题可以作为二叉树演变情况的基础

 """
 
 
 # Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
 
    def traversal_all_the_path(self, root):
        rs = []
        if not root:
            return rs
        self.helper3(root, [], rs)
        return rs
    def helper3(self, root, curRs,rs):
        if not root.left and not root.right:
            """
            在第一次进入这个if时，rs=[]，append以后变成了[[第一次的结果]]
            第二次进入是时，rs=[[第一次的cur结果]]，append后[[第一次的结果],[第二次的结果]]
            """
            rs.append(curRs+[root.val])
        if root.left:
            self.helper3(root.left, curRs+[root.val],rs)
        if root.right:
            self.helper3(root.right,curRs+[root.val],rs)


"""
    1
   / \
  2   3
Output: 25

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
"""
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

print(so.traversal_all_the_path(root2))