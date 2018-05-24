"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively. 


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        如果存在左右子树，判断左右子树是否相等
        如果相等，则继续判断：
            左子树根 的 右子树根节点 与 右子树根 的 左子树根节点 是否相等 
            and 
            左子树根 的 左子树根节点 与 右子树根 的 右子树根节点 是否相等
        """

        if root:
            return self.helper(root.left, root.right)
        return True
    def helper(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:      
            return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)
        return False#其他情况，都是不对称

        """ 
        一棵树对称，就是看左右子树是否对称，到了某一个节点，不对称的条件有以下三个：
        1）左边为空而右边不为空
        2）与1）相反
        3）左边的值不等于右边的值
        对于这样一棵树：
                1
               /  \
              2    2
             / \   / \
            3   4 4   3
           /          /
          5          5 
        以下是递归方法
        root = 1
            roo1=1.left2  root2=1.rigt=2
                roo1和root2都非空，递归调用
                (1)root1=2.left=3  root2=2.rigt=3
                roo1和root2都非空，递归调用
                    1))roo1=3.left=5 root2=3.right=None
                    root2为空，进入第二个if，返回False
                所以第一部分为False


                (2)root1=2.rigt=4  root2=2.left=4  
                roo1和root2都非空，递归调用
                    1))root1=4.left=None root2=4.right=None
                    root1和roo2都为空，进入第一个if，返回True
                所以第二部分为True
            所以: False and True，返回False

        """
    def helper_old(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)

    """
    非递归的遍历方法

    """
    def isSymmetric_iterative(self, root):

        return

    def isSymmetric_ori_wrong(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        *************以下是错误的方法和思路**************


           前序遍历：根 左 右
           中序遍历：左 根 右 
           后序遍历：左 右 根

                 1
               /   \
              2     2
             / \   /  \
            3   4 4    3
           / \        / \
          5  6       6   5

          pre: 根 左 右
          [1,2,3,5,6,4,2,4,3,6,5]

          post：左 右 根
          [5,6,3,4,2,4,6,5,3,2,1]
        
         可以观察到，同一棵树，前序遍历的结果reverse以后，如果等于后续遍历的结果，则对称


         ******错误原因分析******
        对于这样一棵树：
                1
               /  \
              2    2
             /     /
            3      3
        前序遍历:[1,2,3,2,3]
        后序遍历:[3,2,3,2,1]
        前序reverse以后等于后续，但不是对称树 

         
         """
        pre = self.preOrder(root)
        post = self.postOrder(root)
        return pre[::-1] == post[:]
    # pre: 根 左 右
    def preOrder(self, root):
        rs, stack = [], []
        if not root:
            return rs
        while root or stack:
            if root:
                rs.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return rs
    #post：左 右 根
    """
            1
          /   \
         2     3
        / \   / \
       4   5 6   7

    """
    def postOrder(self, root):
        rs, stack = [], []
        if not root:
            return rs
        while root or stack:
            while root:
                stack.append((root, False))
                root = root.left
            top, visit = stack.pop()
            # print(top.val)
            if top.right == None or visit == True:
                rs.append(top.val)
            else:
                stack.append((top, True))
                root = top.right

        return rs

so = Solution()

l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(2)
l4 = TreeNode(3)
l5 = TreeNode(4)
l6 = TreeNode(4)
l7 = TreeNode(3)
root = l1

l1.left = l2
l1.right = l3
l2.left = l4 
l2.right = l5
l3.left = l6
l3.right = l7

# print(so.isSymmetric(root))

l1 = TreeNode(1)

l21 = TreeNode(2)
l22 = TreeNode(2)

l31 = TreeNode(3)
l32 = TreeNode(4)
l33 = TreeNode(4)
l34 = TreeNode(3)

l41 = TreeNode(5)
l42 = TreeNode(6)
l43 = TreeNode(6)
l44 = TreeNode(5)

root = l1

l1.left = l21; l1.right = l22

l21.left = l31; l21.right = l32
l22.left = l33; l22.right = l34

l31.left = l41; l31.right = l42
l34.left = l43; l34.right = l44
print(so.isSymmetric(root))

