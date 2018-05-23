"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
递归调用，对每一个节点进行比较
ref:
    https://leetcode.com/problems/same-tree/discuss/32729/Shortest+simplest-Python
    https://leetcode.com/problems/same-tree/discuss/126574/Easy-to-Understand-Python-Beats-98


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        """
        my origin code:
            if not p  and not q :
                return True
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left)  and self.isSameTree(p.right, q.right)
        报错，因为
        第一个判断是and，所以如果p是none，而q不是none，不会进入if而是继续往下走
        这时候，p.val就不存在（因为p是none）
        所以只有p和q都不是none的时候，才有比较的意义，但如果加上p和q的非空判断：
         if p and q and p.val != q.val:return false
         还是不行，why?,因为：
        如果testcase如下的时候回报错：
            1       1
           /         \
          2           2
        1)p and q成立！ p.val = 1 = q.val = 1成立
        2)所以调用isSameTree(p.left,q.left)
         但此时,q是没有left的，所以isSameTree(p.left, q.left) 报错
        3)所以需要加上判断:
        if p.left and q.left and p.right and q.right:
            return self.isSameTree(p.left, q.left)  and self.isSameTree(p.right, q.right)
         但是这样写台繁琐，而且容易考虑不全，所以转换思想：只有p和q有意义且相等的时候才有进一步比较的意义，
         除此之外的其他情况，都不用比较，都是错的，所以改为：以下的代码
        """
        if not p  and not q :
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left)  and self.isSameTree(p.right, q.right)
        else:#其他情况都是false
            return False

        

l11 = TreeNode(1)
l12 = TreeNode(2)
l13 = TreeNode(3)

l21 = TreeNode(1)
l22 = TreeNode(2)
l23 = TreeNode(3)

p = l11
q = l21

l11.left = l12
l11.right = l13

l21.left = l22
l21.right = l23

p11 = TreeNode(1)
p12 = TreeNode(2)

q11 = TreeNode(1)
q12 = TreeNode(2)

p = p11
q = q11
p11.left = p12
q11.right = q12


so = Solution()
res = so.isSameTree(p,q)
print(res)