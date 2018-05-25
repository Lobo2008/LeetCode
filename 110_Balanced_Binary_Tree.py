"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7

Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

Return false.


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """


        """
        rs = self.height(root)
        return rs != -1
        """
             1
           /   \
          2     3
         / \   / \
        4   5  
       /
      8 
        root = 1
            left=h(1.left=2)
                ->root=2
                    left=h(2.left=4)
                        ->root=4
                            left=h(4.left=8)
                                ->root=8
                                    left=h(8.left=None),所以返回0,即left=0 < 0不成立，继续往下走
                                    rigt=h(8.rigt=None),所以返回0,即rigt=0 < 0不成立，继续往下走
                                    abs(l,r)>1不成立，继续往下走
                                    返回max(0,0)+1 = 1
                                    【所以root=8时返回】
                            所以left=1<0不成立，继续往下走
                            rigt=h(4.right=None),所以返回0,即righ=0<0不成立，往下走
                            abs(l,r)=1>1不成立，往下走
                            返回max(1,0)+1=2
                            【所以root=4时返回2】
                    所以left=2<0不成立，继续往下走
                    rigt=h(2.right=5)
                        ->root=5
                            left=h(5.left=None),所以返回0，即left=0<0不成立，继续往下走
                            rigt=h(5.rigt=None),所以返回0，即rigt=0<0不成立，继续往下走
                            abs(l,r)=0>1不成立，继续往下走
                            返回max(0,0)+1=1
                            【所以root=5时返回1】
                    所以rigt=1<0不成立，继续往下走
                    abs(l,r)=1>1不成立，继续往下走
                    返回max(2,1)+1 = 3
                    【所以root=2时返回3】
            所以left=3<0不成立，继续往下走
            rigt=h(1.rigt=3)
                ->root=3
                    left=h(3.left=None),所以返回0，即left=0<0不成立，继续往下走
                    rigt=h(3.rigt=None),所以返回0，即left=0<0不成立，继续往下走
                    abs(l,r)=0>1不成立，继续往下走
                    返回max(0,0)+1
                    【所以root=3时返回1】
            所以rigt=1<0不成立，继续往下走
            abs(3,1)=2>1成立，所以返回-1 
            【所以root=1时返回-1】
        返回-1，则说明不平衡，False    
             1
           /   \
          2     3
         / \   / \
        4   5  
       /
      8                       
        """
    def height(self, root):
        if root is None:
            return 0
        left = self.height(root.left)
        if left < 0:
            return -1
        right = self.height(root.right)
        if right < 0:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1

so = Solution()

l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
l4 = TreeNode(4)
l5 = TreeNode(5)
# l6 = TreeNode(6)
# l7 = TreeNode(7)
l8 = TreeNode(8)

root = l1

l1.left = l2
l1.right = l3
l2.left = l4
l2.right = l5
# l3.left = l6
# l3.right = l7 
l4.left = l8
print(so.isBalanced(root))