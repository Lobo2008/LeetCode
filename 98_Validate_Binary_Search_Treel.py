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

        回忆一下，对一棵BST，对其进行中序遍历（左-root-右），会得到一个升序排列的数组
        所以，利用这个思路进行处理，如果这棵树中序遍历的结果不是一个升序数组，就返回false：
        """
        if not root:
                return True
        stack=[]
        nowMax = -10**10
        while root or stack:
                if root:
                        stack.append(root)
                        root = root.left
                else:
                        """
                        因为是升序排列的，所以第n个数应该比n-1个数大，
                        第n个数就是pop出来的元素，n-1就是当前最大值
                        如果不满足这个条件，说明不是升序排列，就直接返回，不用继续下去
                        """
                        root = stack.pop()
                        if root.val <= nowMax:
                                return False
                        nowMax = root.val
                        root = root.right
        return True
                
        

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
