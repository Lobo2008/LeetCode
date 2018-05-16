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
        stack = []
        rs = []
        """
        
           1
          /   \
         2     3
        / \   / \
       4   5 6   7
       
       中序遍历：左->中->右
        当节点nodex没有leftsun的时候，弹出nodex，然后访问nodex的根，然后再访问rightsun

       1)root 存在(1)，则继续往其leftson(2)走过去，一直走到leftson不存在的时候(在if里面)
          同时，每次都把走过的节点压入栈stack中，所以 stack=[1] -> [1,2] ->[1,2,4]
       2)当走到4的时候，root = null,这时候while的第一个条件不成立，但此时stack有数据，所以循环仍继续
           if不成立，此时stack=[1,2,4]  进入 else：
           因为4没有leftsun，所以弹出栈的top元素，第一个结果就是当前节点[4],
           接着访问4的daddy 2 [4,2]，daddy2存在rightson 5
            访问rightson，因为rightson没有左右子节点->[4,2,5]，所以daddy2已经处理完，
        3)daddy2 变成son2，是daddy1的leftsun2,已经访问完，所以访问daddy1->[4,2,5,1]
          daddy1存在右儿子，访问rightson3
        4）rightson3有leftson6          

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
    ->  4)root不存在,进入else，stack弹出4后=[1,2]    root=pop=4          rs=[4]     root=4.right=null
        5)root不存在,进入else，stack弹出2后=[1]      root=pop=2          rs=[4,2]   root=2.right=5
        6)root存在(5)，进入if，stack=[1,5]          root=5.left=null    rs=[4,2]
        7)root不存在,进入else，stack弹出5后=[1]      root=5              rs=[4,2,5] root=5.right=null
        8)root不存在,进入else，stack弹出1后=[]       root=1              rs=[4,2,5,1] root=1.right
        9)root存在(3)，进入if。。。。。。

        注意 看4），当节点不存在，即最【左】叶子不存在的时候，访问当前元素null的根4，栈top元素就是当前元素的dad，所以将【中】
        放入rs,
        然后再将【右】son作为根进行访问
        
        """


        while root or stack:
            if root:
                print('---if:',root.val)
                stack.append(root)
                root = root.left
            else:
                
                root = stack.pop()
                print('---el:',root.val)
                rs.append(root.val)
                root = root.right
        return rs

so = Solution()

#[1,null,2,3]
"""
Input: [1,null,2,3]
   1
    \
     2
    /
   3
"""

"""
l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
root = l1
l1.right = l2
l2.left = l3
"""


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

print(so.inorderTraversal(root)) #这里参数传 l1 和 root都可以
