"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        对于每一层：
            从左到右
            从右到左
            从左到右
            依次类推

        都可以基于level order来改变，奇数就直接append本层的结果，偶数层先reverse本层的结果，再放入结果集中即可
        """
        rs = []
        if root == None:
            return rs
        thisLevel = [root]
        even_odd = 1
        while thisLevel:
            levelrs = []
            nextLevel = []
            for node in thisLevel:#对每个节点进行操作，当前节点放入本层结果集中，左右儿子放入下一层结果集
                levelrs.append(node.val)#把当前节点加入本层的结果集当中
                if node.left:#有leftson，则放入下一层待遍历的结果集
                    nextLevel.append(node.left)
                if node.right:#有rightson，则放入下一层待遍历的结果集
                    nextLevel.append(node.right)
            if even_odd % 2 == 0:#每一层的顺序不一样，用奇偶性进行控制
                levelrs.reverse()
            even_odd += 1
            rs.append(levelrs)
            thisLevel = nextLevel
        return rs


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



print(so.zigzagLevelOrder(root))
