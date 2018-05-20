"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
               1
             /   \
            2     3
           / \    / \
          4   5  6   7
        遍历方法，仍然用到了层序遍历的思想
        """
        level = [root]
        if not root:
            return 0
        levelnum = 0
        while level:
            nextlevel = []
            levelnum += 1
            for node in level:
                if node.left:
                    nextlevel.append(node.left)
                if node.right: 
                     nextlevel.append(node.right)
            level = nextlevel
        return levelnum
    """
    递归方法

    """
    def maxDepth_recurssive(self, root):
        if not root:
            return 0
        return 1+max(self.maxDepth_recurssive(root.left), self.maxDepth_recurssive(root.right))
            
        
so = Solution()

l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
l4 = TreeNode(4)
l5 = TreeNode(5)
l6 = TreeNode(6)
l7 = TreeNode(7)

root = l1

l1.left = l2
l1.right = l3
l2.left = l4
l2.right = l5
l3.left = l6
l3.right = l7 



print(so.maxDepth(root))
print(so.maxDepth_recurssive(root))