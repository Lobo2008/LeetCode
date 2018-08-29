"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.



"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        从根开始的每一个树，组合成一个数字，取所有的数字的和，得到结果返回
        需要得到所有子树

        根后续遍历有一点像，
        """
    
        """
        1)[4]
        2)[4]+
            [9]
                [5]
                [1]
            [0]
        level:
            [4]
            [9,0]
            [5,1]
            4
           / \
          9   0
         / \
        5   1

        """
        return self.helper(root, 0)
    def helper(self, root, sum):
        if not root:
            return 0
        if not root.left and not root.right:
            return sum*10 + root.val
        return self.helper(root.left,sum*10+ root.val) + \
                self.helper(root.right,sum*10 + root.val)
        """       
            4
           / \
          9   0
         / \
        5   1
        root = 4 cur=[] rs=[]
            left=h(4.left=9,cur=[]+[4],rs=[]) -> h(9,[4],[])
                root=9 cur=[4] rs=[]
                    left=h(9.left=5,cur=[4]+[9],rs=[]) -> h(5,[4,9],[])
                        root=5 cur=[4,9] rs=[]
                            ->not root.left and not root.right,rs=[[4,9]+[5]] = [[4,9,5]]
                    rigt=h(9.rigt=1,cur=[4]+[9],rs=[[5,9,5]]) -> h(1,[4,9],[[4,9,5]])
                        root=1 cur=[4,9] rs=[[4,9,5]]
                            ->  ->not root.left and not root.right,rs=[[4,9,5]+[4,9]+[1]=[[4,9,5],[4,9,1]]
            rigt=h(4.rigt=0,cur=[4],rs=xx)
        """
    def sumNumbers2(self, root):
        rs = []
        if not root:
            return 0
        self.helper2(root, [], rs)#因为not root的情况已经判断了，所以helper2里面的root必定非None
        sum = 0
        for item in rs:
            l = len(item)
            for i in range(l):
                sum += item[i]*(10**(l-i-1))
        return sum
    def helper2(self, root, curRs, rs):
        """
        因为sumNumbers2中传进helper2的root必定非none，
        同时，helper2自己调用的root.left等因为做了判断（非none才调用），所以不用再次判断if not root的情况
        """
        if not root.left and not root.right:
            """
            if rs=[],cur=[4],then rs.append(cur) = [[4]]
            if rs=[],cur=4,  then rs.append(cur) =  [4], notice the diffrence
            """
            rs.append(curRs + [root.val])
        if root.left:
            self.helper2(root.left, curRs+[root.val],rs)
        if root.right:
            self.helper2(root.right, curRs+[root.val], rs)




    
"""
    1
   / \
  2   3
Output: 25

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
"""
so = Solution()

l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
root1 = l1
l1.left = l2; l1.right = l3

t1 = TreeNode(4)
t2 = TreeNode(9)
t3 = TreeNode(0)
t5 = TreeNode(5)
t6 = TreeNode(1)
root2 = t1
t1.left = t2; t1.right = t3
t2.left = t5; t2.right = t6

# print(so.sumNumbers(root1))
print(so.sumNumbers2(root2))





