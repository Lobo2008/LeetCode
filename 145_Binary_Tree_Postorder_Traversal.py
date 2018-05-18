"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        """
        后序遍历：左-右-根


        1
      /   \
     2     3
    / \   / \
   4   5 6   7
        1）root=1
            (1) root=1  stack=[1]     root=1.left=2
                root=2  stack=[1,2]   root=2.left=4
                root=4  stack=[1,2,4] root=4.left=none
                root=null  while终止循环，此时stack=[(1,x),(2,x),(4,x)]

            (2)top=4,visi=Fals
                4.right=None，所以进入if  => rs=[4]，此时stack=[(1,x),(2,x)]
        2)stack !=0
            (1) root=none，所以不进入while循环
            (2)top=2,visi=False
                2.right=5且visi!=True 所以进入Else：把刚弹出的元素标记以后再压入栈-> stack=[(1,x),(2,v)]
                root=2.right=5
        3)root=5，
            (1)root=5 说明该遍历5为根的这可树了
                ...
                whilez终止循环时，stack=[1x,2v,5x],root=none
            (2)top=5,visi=False
                5.right=None，所以进入if => rs=[4,5]， 此时stack=[(1,x),(2,v)]
        4)stack !=0
            (1)root=none，所以不进入while循环
            (2)top=2,visi=True
              因为visi=True，表明这个节点访问过，说明是从右son回来的，所以进入if => rs=[4,5,2]
                                                            此时stack=[(1,x)]
        5)stack !=0
             (1)root=none，所以不进入while循环
             (2)top=1,visi=False
                因为1.right=3且visi=False，所以进入else，说明要访问1的右子树了，把1标记，此时
                stack=[(1,v)]  root=1.right=3
        6)root=3
           ...
        


        """
        stack = []
        rs = []
        while root or stack:
            """
            一直往左找到树的左儿子节点，比如第一次是[1,2,4]  4.left=none，所以已经到底了
            """
            while root:
                stack.append((root, False))
                root = root.left
            """
            先访问栈顶元素：
                1）如果栈顶元素还有右son，则往右son走（因为是从上面的while访问左son来的，现在轮到右son了）
                2）如果栈顶没有右son，或者栈顶已经访问过一次，，则该节点就是结果，放入rs中
            """
            top, visited = stack.pop()#先访问栈顶的4
           
            if top.right == None or visited == True:
                rs.append(top.val)
            else:
                stack.append((top, True))
                root = top.right

        return rs

    """

    ref:leetcode.com/problems/binary-tree-postorder-traversal/discuss/45559/My-Accepted-code-with-explaination.-Does-anyone-have-a-better-idea/118572
    """
    def postorderTraversalX(self, root):
        stack,result = [],[]
        testStack=[]
        while(root or len(stack) > 0):
            print('--------')
            while(root):
                print('--small while')
                stack.append((root,False))
                testStack.append((root.val,False))
                root = root.left
            print(testStack)
            top,visited = stack.pop()
            testStack.pop()
            print(' ',top.val,visited)
            if(top.right is None or visited is True):
                print('  in if')
                result.append(top.val)
            else:
                print('  in else')
                stack.append((top,True))
                testStack.append((top.val,True))
                root = top.right
            print('     ->',result)
        return result

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


print(so.postorderTraversal(root))
# print(so.postorderTraversalX(root))