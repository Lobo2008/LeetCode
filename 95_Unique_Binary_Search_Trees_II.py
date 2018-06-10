"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        """
        这次不仅是要算数量，还要把具体的树给求出来

    
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
    n = 3, help(1,3)

    l=1,r=3,rs=[]
        if  x
        i=1, 以1为根的情况
            left=h(l,i-1)=h(1,0) 因为l > r:所以 None->rs=[None] => [None]      
            rigt=h(i+1,r)=h(2,3)
                l=2,r=3,rs=[]
                    if  x
                    i=2， 以2为根的情况（注意，这个2根的daddy是1）
                        left=h(l,i-1)=h(2,1) 因为l > r:所以 None->rs=[None] => [None] 
                        rigt=h(i+1,r)=h(3,3)
                            l=3,r=3,rs=[]
                                if  x
                                i=3，以3为根的情况（注意，这个根3的daddy是2）
                                    left=h(l,i-1)=h(3,2) 因为l > r:所以 None->rs=[None] => [None]
                                    rigt=h(i+1,r)=h(4,3) 因为l > r:所以 None->rs=[None] => [None]
                                    所以left=[None],rigt=[None]
                                    j=0
                                        k=0
                                            root=T(i)=T(3)
                                            root.left=left[j]=None
                                            root.rigt=rigt[k]=None 
                                            rs=[3]，一个根为3的树，没有子节点
                        所以left=[None],right=[3]
                        j=0 
                            k=0
                                root=T(i)=T(2)
                                root.left=left[j]=left[0]=None
                                root.rigt=rigt[k]=rigt[0]=3
                                rs=[2,null,3]
                                      1
                                       \
                                        2
                                         \
                                          3 
                    i=3
                        left=h(l,i-1)=h(2,2)
                            l=2,r=2,rs=[]
                                if x
                                i=2
                                    left=h(l,i-1)=h(2,1) 因为l > r:所以 None
                                    rigt=h(i+1,r)=h(3,2) 因为l > r:所以 None
                                    j循环 x
                                    k循环 x
                        rigt=h(i+1,r)=h(4,3)因为l > r:所以 None
                        j循环 x
                        k循环 x
        #l=1,r=3,rs=[]
        i=2 
            left=h(l,i-1)=h(1,1)
            rigt=h(i+1,r)=h(3,3)
        i=3
            left=h(l,i-1)=h(1,2)
            rigt=h(i+1,r)=h(4,3) 因为l > r:所以 None

    
        """
        if n == 0:return []
        return self.helper(1,n)

    def helper(self, left, right):
            rs = []
            if left > right:
                rs.append(None)
                return rs
            for i in range(left, right+1):#range(2)=2~n-1，但也要讨论n的情况，所以加个1
                leftLs = self.helper(left, i-1)
                rightLs = self.helper(i+1, right)
                for j in range(len(leftLs)):
                    for k in range(len(rightLs)):
                        root = TreeNode(i)
                        root.left = leftLs[j]
                        root.right = rightLs[k]
                        rs.append(root)
            return rs

        
so = Solution()
n = 2
print(so.generateTrees(n))