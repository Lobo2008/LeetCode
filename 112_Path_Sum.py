"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        """
        root-to-leaf 
        注意，是root到子叶节点，所以必须是一条完整的路径

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
        root = 5, sum=22
            has(5.left=4, 22-5=17) => has(4,17)
                root=4,sum=17
                    has(4.left=11, 17-4=13) => has(11,13)
                        root=11,sum=13
                            has(11.left=7,sum=13-11=2) => has(7,2)
                                ...
                            has(11.rigt=2,sum=13-11=2) => has(2,2)
                                root=2,sum=2
                                    root.left=root.right=none and root=sum:
                                    返回True
                            返回True
                    返回True
                返回True
                    has(4.righ=none)        => has(none,13)
            has(5.rigt=8, 22-5=17) => has(8,18)

        简化版，sum=9
              5
             / \
            4   8
        root=5,sum=9
            has(5.left=4,9-5=4) => has(4,4)
                root=4,sum=4
                    has(4.left=none,x) => has(none,x)  因为root.val=sum，返回true
            has(5.rigt=8,9-5=4) => has(8,4)
                ...
        """

        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
"""
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
"""
so = Solution()

l1 = TreeNode(5)

l21 = TreeNode(4)
l22 = TreeNode(8)

l31 = TreeNode(11)
l32 = TreeNode(13)
l33 = TreeNode(4)

l41 =TreeNode(7)
l42 = TreeNode(2)
l43 = TreeNode(1)

root = l1

l1.left = l21; l1.right = l22

l21.left = l31; l22.left= l32; l22.right = l33

l31.left = l41; l31.right = l42; l33.right = l43

sum = 22
print(so.hasPathSum(root,sum))
