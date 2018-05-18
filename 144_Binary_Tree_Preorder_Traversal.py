"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

Follow up: Recursive solution is trivial, could you do it iteratively?


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        前序遍历：根-左-右

        1）root=1存在，rs=[1] ->=[2,4,5]  ->r=[3,6,7]  ==>[1,2,4,5,3,6,7]
        2)访问左子树，存在
             2
           /  \
          4    5  
            (1)root=2存在, rs_l=[2] ->[2,4,5]
            (2)访问左子树，存在  -> rs_l_l=[4]
                  4
                /   \
               no1  no2
                  root=4,存在，rs_l_l=[4]
                  访问左子树，不存在 ，rs_l_l=[4]
                  访问右子树，不存在 ，rs_l_l=[4]
                所以rs_l_l=[4]
             (3)访问右子树，存在rl_r_r= =[5]
        3)访问右子树，存在  -> [3,6,7]
            3
          /   \
         6     7  


     1)root=1 存在，rs=[1],     stack=[1],    root=left=2
     2)root=2 存在，rs=[1,2],   stack=[1,2]     root=left=4
     3)root=4 存在，rs=[1,2,4], stack=[1,2,4]   root =left=null
     4)root=null不存在，stack弹出4->stack=[1,2]  相当于返回dad，root=4,然后访问右son，right=null
     5)root=null不存在，stack弹出2->stack=[1]    相当于返回dad，root=2，然后访问右son，right=5
     6)root=5 存在，rs=[1,2,4,5] stack=[1,5]  root=left=null
     7)......
"""
        rs = []
        stack = []
        while root or stack:
            if root:
                rs.append(root.val)
                stack.append(root) ####注意！！易错点，是append(root), 不是root.val
                root = root.left
            else: 
                root = stack.pop()
                root = root.right
        return rs

    """
    前序遍历，递归方法
    """    
    def preorderTraversal_recursive(self, root):

        rs = []
        self.recursive(root, rs)
        return rs
    def recursive(self, root,rs):
        if root:
            rs.append(root.val)
            self.recursive(root.left, rs)
            self.recursive(root.right, rs)


        
so = Solution()

"""

        1
      /   \
     2     3
    / \   / \
   4   5 6   7

"""

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

print(so.preorderTraversal(root))
# print(so.preorderTraversal_recursive(root))