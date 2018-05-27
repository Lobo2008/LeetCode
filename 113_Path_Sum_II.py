"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        """ 
        root-to-leaf ,sum = 20
              5
             / \
            4   8
           /   / \
          11  13  7
        root=5, sum=20
            left=(5.left=4,20-5=15) => left(4,15)
                root=4,sum=15
                    left=(4.left=11,15-4=11) => left(11,11)
                        root=11,sum=11
                            root.left=root.rigt=none and root.val=sum，所以返回[[sum]] = [[11]]
                    所以rs=[4]+[11]=[4,11]
                    rigt=(4.rigt=none)       => rigt(none),为空，所以返回[]
                    因为rigt为空，所以两个for循环以后rs还是[4,11]
                所以返回[4,11]
            所以rs=[5]+[4,11]=[5,4,11] 

            rigt=(5.rigt=8,20-5=15) => rigt(8,15)
                root=8,sum=15
                    left=(8.left=13,15-8=7) => left(13,7)
                        root=13,sum=7
                            root.left=root.rigt=none and root.val!=sum，所以返回[]
                    rigt=(8.rigt=7 ,15-8=7) => rigt(7,7)
                        root=7,sum=7
                            root.left=root.rigt=none and root.val=sum,收益以返回[[7]]
                所以for循环以后rs=[8] + [7] =[8,7]
            所以rs=[5]+[8]+[7] =[5,8,7]
        """
        #ref：https://www.cnblogs.com/chruny/p/5258576.html
        rs = []
        if not root:
            return rs
        if not root.left and not root.right:
            if  root.val == sum:
                return [[sum]]
            else:
                return []
        left =  self.pathSum(root.left, sum-root.val)
        right = self.pathSum(root.right, sum-root.val) 
        for item in left:
            rs.append([root.val] + item)
        for item in right:
            rs.append([root.val] + item)
        return rs
    #ref：https://blog.csdn.net/u013291394/article/details/50740194
    def pathSum2(self, root, sum):
        rs = []
        self.helper2(root,sum,[], rs)
        return rs
    """
              5
             / \
            4   8
           /   / \
          11  13  7
        这种方法，在helper里面没有直接返回rs，而是在调用helper的那个方法里面返回的
    """

    def helper2(self, root, sum, currRs, rs):
        if not root:
            return
        sum -= root.val
        """
        到达叶子节点，切叶子节点的值等于当前sum的值，就放到rs里面
        """
        if sum == 0 and not root.left and not root.right:
            rs.append(currRs + [root.val])
        if root.left:
            self.helper2(root.left, sum, currRs+[root.val], rs)
        if root.right:
            self.helper2(root.right, sum, currRs+[root.val], rs)
"""
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
"""        

so = Solution()

l1 = TreeNode(5)

l21 = TreeNode(4)
l22 = TreeNode(8)

l31 = TreeNode(11)
l32 = TreeNode(13)
l33 = TreeNode(4)

l41 =TreeNode(7)
l42 = TreeNode(2)
l43 = TreeNode(5)
l44 = TreeNode(1)

root = l1

l1.left = l21; l1.right = l22

l21.left = l31; l22.left= l32; l22.right = l33

l31.left = l41; l31.right = l42; l33.left = l43; l33.right = l44

sum = 22
print(so.pathSum(root,sum))
print(so.pathSum2(root,sum))