"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        """
        给一个前序遍历的list和一个中序遍历的list，将其恢复成二叉树
        前序遍历preorder： root-左-右
        中序遍历inorder：  左-root-右
        preorder = [3,9,2,20,15,7]
        inorder = [2,9,3,15,20,7]
               3
              / \
             9  20
            /  /  \
           2  15   7
        1)p=[3,9,2,20,15,7], in=[2,9,3,15,20,7]
            node=3,此时p=[9,2,20,15,7],in=[2,9,3,15,20,7],index=2 #找到一个node3
            left=h(p,in[:2]) #下面开始找3的左son
                p=[9,2,20,15,7],in=[2,9]
                    node=9,此时p=[2,20,15,7],in=[2,9],index=1 #找到3的左son是9
                    left=h(p,in[:1]) #再接着找9的左son
                        p=[2,20,15,7],in=[2]
                            node=2,此时p=[20,15,7],index=0 #找到9的左son是2，接着找2的左son
                                3
                               /
                              9
                             /
                            2    
                            left=h(p,in[:0]) #找2的左son
                                p=[20,15,7],in=[]   not in成立，return None #2不存在左son
                            rigt=h(p,in[1:]) #找2的右son
                                p=[20,15,7],in=[]   not in成立，return None #2不存在右son

                    rigt=h(p,in[2:]) #再接着找9的右son
                        p=[2,20,15,7],in=[] not in成立，return None #不9存在右son
                    
                    至此p=[20,15,7]

            rigt=h(p,in[3:]) # 下面开始找3的右son 
                p=[20,15,7],in=[15,20,7]
                    node=20,此时p=[15,7],in=[15,20,7],index=1 #找到3的右son是20
                    left=h(p,in[:1])#开始找20的左son
                        p=[15,7],in=[15]
                            node=15,此时p=[7],in=[15],index=0 #找到20的左son是15
                            left=h(p,in[:0])#再找15的左son，不存在
                            rigt=h(p,in[1:]#找15的右son，不存在
                    rigt=h(p,in][2:])#开始找20的右son
                        p=[7],in=[7]
                            node=7,此时p=p[],in=[7],index=0 #找到20的右son是7
                            left=。。。#开始找7的左son
                            ...


                            所以    3
                                    \
                                     20
                                     / \
                                    15  7
        还是递归啊。。。。。
        简化版
            3
           / \
          4   5

        p=[3,4,5]
        in=[4,3,5]

        node=3,此时p=[4,5],in=[4,3,5],index=1  找到根3
        left=h(p,in[:1])#开始找3的左son
            p=[4,5],in=[[4]
                node=4,此时p=[5],in=[4],index=0 找到3的左son是4
                left=h(p,in[:0])，不存在
                rigt=h(p,in[1:]),不存在
                至此，p=[5]
        rigt=h[p,in[2:]]#开始找3的右son
            p=[5],in=[5]
                node=5,此时p=[],in=5,idnex=0 找到3的右son是5
                left=不存在
                rigt=不存在
        """
        if not preorder or not inorder:
            return None
        node = TreeNode(preorder.pop(0))
        index = inorder.index(node.val)
        node.left = self.buildTree(preorder, inorder[:index])
        node.right = self.buildTree(preorder, inorder[index+1:])
        return node

    """
    [3,9,20,15,7]
    """

so = Solution()
preorder = [3,9,2,20,15,7]
inorder = [2,9,3,15,20,7]

print(so.buildTree(preorder, inorder))