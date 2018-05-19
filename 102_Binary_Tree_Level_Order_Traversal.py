"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        """

               1
             /   \
             2     3
            / \   / \
          4   5 6   7

        1）第一层[1]
          (1)node=1, levelrs=[1], 1.left=2,1.right=2，一个node只有left和right两个节点
             -> next=[2,3]    rs=[[1]]
        2)第二次[2,3]
          (1)node = 2, levelrs=[2], 2.left=4, 2.right=5   ->next=[4,5]
          (2)node = 3, levelrs=[3], 3.left=6, 3.right=7  ->next=[4,5,6,7]
          ->rs=[[1],[2,3]]
        3)第三层[4,5,6,7]
           (1)node=4, levelrs=[4] 4.left=None,4.right=None   ->next=[]
           (2)node=5....
           ...
            ->levelrs=[4,5,6,7]
            ->rs=[[1],[,3],[4,5,6,7]]
        """

        rs = []
        if root == None:
            return rs
        thisLevel = [root]
        while thisLevel:
            levelrs = []
            nextLevel = []
            for node in thisLevel:#遍历当前层的所有节点
                levelrs.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            rs.append(levelrs)
            thisLevel = nextLevel#新的遍历的集就是层遍历的下一层
        return rs

"""

        1
      /   \
     2     3
    / \   / \
   4   5 6   7

"""

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



print(so.levelOrder(root))

