"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        """
        给定一个升序的list，返回一棵二叉搜索树，
        二叉搜索树的定义：
            它或者是一棵空树，或者是具有下列性质的二叉树： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。
        简单的说，就是满足：左 < 根 < 右
        [-10,-3,0,5,9]
              0
             / \
           -3   9
           /   /
         -10  5
        len(nums)-1=4,so r = 4
        l=0,r=4, -> mid = (0+4+1)//2=2
            root=n[2]=0 #找到根0
                left=h(0,mid-1)=h(0,1)#开始查找0的左son
                    l=0,r=1 -> mid=(0+1+1)//2=1
                        root=n[1]=-3 # 0的左son就是-3，然后再找-3的左son
                                0
                               /
                              3 
                            left=h(0,mid-1)=h(0,0)
                                l=0,r=0 -> mid=(0+0+1)//2=0
                                    root=n[0]=-10 #-3的左son就是-10
                                        left=h(0,mid-1)=h(0,-1)
                                            l=0,r=-1 因为l>r所以直接返回，说明-10没有左son  
                                        rigt=h(mid+1,r)=h(1,0)
                                            l=1,r=0  因为l>r所以直接返回，说明-10没有右son       
                            rigt=h(mid+1,r)=h(2,1) #找-3的右son
                                l=2,r=1因为l>r所以直接返回，说明-3没有右son        
                
                rigt=h(mid+1,r)=h(3,4)#开始找0的右son
                    l=3,r=4 -> mid=(3+4+1)//2=4
                        root=n[4]=9 # 0的右son就是9，然后再找9的左son
                            0
                             \
                              9
                            left=xxxx
        关于 mid=(l+r)//2还是mid=(l+r+1)//2，可以找一个长度为5的nums试一下就可以

        另外，可以注意到，这棵树进行中序遍历的结果就是这个nums，所以讲一颗二叉搜索树进行中序遍历以后的结果是一个有序的list

        在python3之前，3/2=1,而在python3及其以后，3/2=1.5，所以在nums[a/b]的时候要换成 nums[int(a/b)]
        [-10,-3,0,5,9]
              0
             / \
           -3   9
           /   /
         -10  5

        """
        if not nums:
            return []
        return self.helper(nums, 0,len(nums)-1)
    def helper(self, nums, left, right):
        if left > right:
            return
        mid = (left + right + 1)//2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums,left,mid - 1)
        root.right = self.helper(nums, mid+1, right)
        return root
    """
    把上面的left 和right都去了，简化代码
    """

    def sortedArrayToBST2(self, nums):
        l = len(nums)
        if l == 0:
            return None
        if l == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[int(l/2)])
        root.left = self.sortedArrayToBST2(nums[:int(l/2)])
        root.right =self.sortedArrayToBST2(nums[int(l/2)+1:])
        return root



so = Solution()

nums = [-10,-3,0,5,9]
rs = (so.sortedArrayToBST(nums))
rs = (so.sortedArrayToBST2(nums))


    