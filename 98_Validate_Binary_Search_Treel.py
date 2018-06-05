"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        给定一棵树，判断是不是平衡BST，也就是是否满足：左son < root < 右son
        递归处理，只要不满足，就return
        注意题目要求：
                root的左son必须小于root
                root的右son必须大于root
                因此，小于等于或者大于等于的时候都是错的
                同时，root的左son的所有节点的值都必须小于root，因此
                4
               /
              3
             / \
            1   5
            这种树，虽然满足了root的左son小于root，但左son的右son大于root，所以是错的 

        """
        if not root:
                return True
        if root:
                if root.left:
                        if root.left.val >= root.val:return False

                        if root.left.left:
                                if root.left.left.val >= root.left.val or \
                                        root.left.left.val >= root.val: return False

                        
                        if root.left.right:
                                if root.left.right <= root.left.val or \
                                        root.left.right >= root.val: return False
                                
                if root.right:
                        if root.right.val <= root.val:return False
                        
                        if root.right.left:
                                if root.right.left.val >= root.right.val or \
                                        root.right.left.val <= root.val: return False
                                
                        if root.right.right:
                                if root.right.right.val <= root.right.val or \
                                        root.right.right.val <=root.val: return False
                return self.isValidBST(root.left) and self.isValidBST(root.right)
        return True



                #         if root.left.val >= root.val:
                #                 return False
                #         if root.left.left and root.left.left.val >= root.left.val or \
                #                 root.left.left.val >= root.val:
                #                 return False
                #         if root.left.right and root.left.right.val <= root.left.val or \
                #                 root.left.right >= root.val:
                #                 return False
                # if root.right:
                #         if root.right.val <= root.val:
                #                 return False

                #         if root.right.right and root.right.right.val <= root.right.val or \
                #                 root.right.__le__



#     def helper(self, root,daddy):
#         if daddy is None:
#         if root:
#                 if root.left and (root.val <= root.left.val or root.left.val >= daddy):
#                         return False
#                 if root.right and (root.val >= root.right.val or root.right.val):
#                         return False
#                 return self.isValidBST(root.left) and self.isValidBST(root.right)
#         return True
        

"""
    5
   / \
  1   4
     / \
    3   6
"""
so = Solution()

t1 = TreeNode(5)
t2 = TreeNode(1)
t3 = TreeNode(4)
t4 = TreeNode(3)
t5 = TreeNode(6)

root = t1

t1.left = t2; t1.right = t3
t3.left = t4; t3.right = t5

print(so.isValidBST(root))
