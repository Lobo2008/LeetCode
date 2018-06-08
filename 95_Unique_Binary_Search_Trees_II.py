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
        """
        if n == 0:return []
        return self.helper(1,n)
    def helper(self, left, right):
            rs = []
            if left > right:
                rs.append(None)
                return rs
            for i in range(left, right+1):
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
n = 5
print(so.generateTrees(n))