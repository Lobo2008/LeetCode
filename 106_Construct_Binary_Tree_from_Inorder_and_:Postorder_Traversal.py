"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        """
        ref:https://www.cnblogs.com/zuoyuan/p/3720138.html

        给一个中序遍历的list和一个后序遍历的list，将其恢复成二叉树
        中序遍历  inorder：  左-root-右
        后序遍历postorder：  左-右-root
        inorder =   [4,2,5,1,6,3,7]
        postorder = [4,5,2,6,7,3,1]
                1
              /   \
             2     3
            / \   /  \
           4   5 6    7

        根据后续遍历可知，po中的最后一个元素1就是root，再在in中找到1相应的位置，in中被1分成了左右两部分
        in左边[4,2,5]，与po中[4,5,2]又组成了一对：
              2
             / \
            4   5
        in= [4,2,5]
        po= [4,5,2]

        递归下去即可

        注意到
        root=pop()以后,root在in中的下标（分界线）是index，则：
        左边部分的一组是 
            in[0:index]     即 [4,2,5]
            po[0:index]     即 [4,5,2]
        右边部分的一组是
            in[index+1:]    即 [6,3,7]
            po[index:]      即 [6,7,3]     因为po用了pop，所以可以直接index: ，否则需变成 index:l-1
        """    
        
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        node = TreeNode(postorder.pop())
        index = inorder.index(node.val)
        node.left = self.buildTree(inorder[:index], postorder[:index])
        node.right = self.buildTree(inorder[index+1:], postorder[index:])
        return node

    """
    这个更快一点
    """
    def buildTree2(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        node = TreeNode(postorder.pop())
        index = inorder.index(node.val)
        
        node.left = self.buildTree2(inorder[:index], postorder[:index])
        node.right = self.buildTree2(inorder[index+1:], postorder[index:])
        return node
"""
[1,2,3,4]
[3,2,1,4]
"""

so = Solution()

inorder   = [2,9,3,15,20,7]
postorder = [2,9,15,7,20,3]

# print(so.buildTree(inorder, postorder))
print(so.buildTree2(inorder, postorder))