"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its minimum depth = 2.

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
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

               1
             /   \
            2     3
           / \    
          4   5  
        遍历方法，仍然用到了层序遍历的思想
        如果root存在一个son，不论是左右，都要继续遍历下一层
        如果root没有son了，就可以终止了
        """
        if not root:
            return 0
        levelnum = 0
        level = [root]
        while level:
            levelnum += 1
            nextlevel = []
            for node in level:
                if not node.left and not node.right:#root没有son，直接返回当前层数
                    return levelnum           
                """
                这里用if if而不用if else的原因：
                      3
                     / \
                    9  20
                       /  \
                      15   7
                如果用if: node.right: append(right)
                    else:           append(left)
                那就会走右边的这一条(3-20),而最短的应该是走3-9这一条
                """
                if node.left:#存在左son
                    nextlevel.append(node.left)
                if node.right:#存在右son
                    nextlevel.append(node.right)
            level = nextlevel
        return levelnum



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
print(so.minDepth(root))
