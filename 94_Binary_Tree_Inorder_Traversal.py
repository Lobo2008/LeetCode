"""
Given a binary tree, return the inorder traversal of its nodes' values.
中序遍历
Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?



ref: https://blog.csdn.net/yangjingjing9/article/details/77054899
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        """       
        非递归方法

       中序遍历：左->中->右
           1
          /   \
         2     3
        / \   / \
       4   5 6   7
     /
    null 
        1)root存在(1)，进入if，stack=[1],           root=1.left=2       rs=[]
        2)root存在(2)，进入if，stack=[1,2],         root=2.left=4       rs=[]
        3)root存在(4)，进入if，stack=[1,2,4]        root.4.left=null    rs=[]
  ->    4)root不存在,进入else，stack弹出4后=[1,2]    root=pop=4          rs=[4]     root=4.right=null
  ->    5)root不存在,进入else，stack弹出2后=[1]      root=pop=2          rs=[4,2]   root=2.right=5
  ->    6)root存在(5)，进入if，stack=[1,5]          root=5.left=null    rs=[4,2]
        7)root不存在,进入else，stack弹出5后=[1]      root=5              rs=[4,2,5] root=5.right=null
        8)root不存在,进入else，stack弹出1后=[]       root=1              rs=[4,2,5,1] root=1.right
        9)root存在(3)，进入if。。。。。。

        注意 看4），当节点不存在，即已经访问到了叶子节点，比如
             4
           /  \
         no1  no2  
        当前的root就是no1
        此时的栈是stack=[xxx,4]
        栈定元素4就是最后一棵树的根（两个空子树）
        所以访问 左-中-右：[no1,4,no2]
            在访问完no1时【左】（else），访问4【中】，然后将root设置为【右】

        左节点访问以后，弹出的元素就是当前子树的父节点，因为访问了父节点，所以按照中序遍历的规则，此时的要访问右节点，所以把root置位rightson
        ...
        当根为4的字数访问完以后，栈顶元素2就是4的daddy，此时获取2以后再讲root设置为2的右son5
              2
           /     \
        4[done]   5
        """
        stack = []
        rs = []
        while root or stack: #栈为空或者已经到叶子的时候停止循环
            if root:#还有左son，就继续往左走
                stack.append(root)
                root = root.left
            else:#没有左son的时候，说明左子树已经遍历完成，然后获取当前的根，再遍历右子树
                root = stack.pop()
                rs.append(root.val)
                root = root.right
        return rs

    """
    中序遍历，递归方法(递归方法比非递归方法快)
         1
       /   \
      2     3
     / \   / \
    4   5 6   7

    递归方法比较好理解，遇到一棵树root，先访问左子树root.left,冉然后访问根节点root，再访问右子树root.right
    递归到最小一棵树的时候返回,
    lets从下往上看,第一棵树
              4
            /   \
         no1     no2
        时，if成立，
           func(4.left=no1)   rs.append(root=4)  func(4.right=no2)
           ->res=[4]
    第二棵树：
            2
           /  \  
          4    5
        时，if成立
           func(2.left=4),就是上面的第一棵树，res=[4]
           func(root=2)                    res=[2]
           func(2.right=5),用第一棵树的方法，可以得到res=[5]，
        ->所以这棵树就是[4,2,5]


    """

    def inorderTraversal_recurssive(self, root):

        res = []
        self.recursive_inOrder(root,res)
        return res

    def recursive_inOrder(self, root, res):
        if root:
            self.recursive_inOrder(root.left, res)
            res.append(root.val)
            self.recursive_inOrder(root.right, res)

so = Solution()

"""
        1
      /   \
     2     3
    / \   / \
   4   5 6   7

注意树的构造方式，
1、先把每个节点  lx = TreeNode(x)给构造了
2、然后把根节点赋值给一个变量root (or etc)
3、接着再把 lx.left 和lx.right的指向给加上
4、最后要用的是root这个变量（应该传递的是指针，所以root就跟l1一样的，但为了更好的区别，另取一个名字）
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

# print(so.inorderTraversal(root)) #这里参数传 l1 和 root都可以
print(so.inorderTraversal_recurssive(root)) #这里参数传 l1 和 root都可以

