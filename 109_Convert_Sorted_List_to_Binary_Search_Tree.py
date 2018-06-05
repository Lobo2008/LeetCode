"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5


"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        """
        给定一个升序链表，返回平衡BST
        有两种方法：
            1.把链表存入数组，然后跟108一样
            2.快慢指针
        以下是方法1
        """
        arr = []
        if head:
            while head:
                arr.append(head.val)
                head = head.next
        return self.helper(arr)
    def helper(self, nums):
        l = len(nums)
        if l == 0:
            return None
        if l == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[int(l/2)])
        root.left = self.helper(nums[:int(l/2)])
        root.right = self.helper(nums[int(l/2)+1:])
        return root

    """
    -10 -> -3 -> 0
    第二种方法，快慢指针，假设只有三个：[-10, -3, 0]
    1)head=-10,tail=None
        if 1 -> x
        if 2 -> x
        mid=head=-10
        fast=head=-10
        因为 fast!=tail and fast.next=-3!=tail
            fast=10.next.next=0
            mid=-10.next=-3
            因为fast!=tail and fast.next=none=tail，所以while循环终止
            此时fast=0
                mid=-3
        node=mid=-3 #找到了一个节点-3
        node.left=h(head,mid)=h(-10,-3) # 然后开始找-3的left
            head=-10,tail=-3
            if 1 ->  x
            head.next=tail,所以if 2 -> v: return head.val=-10
                所以，-3的left就等于-10
            =>此时      -3
                      /
                    -10
        node.right=h(mid.next,tail)=h(0,none) # 然后开始找-3的right
            head=0,tail=none
            if 1 -> x
            head.next=none=tail,所以if 2 -> v: return  head.val=0
                所以-3的right就等于0
            =>此时:     -3
                       / \
                     -10  0  
        快慢指针的point在于
                    -10             -3          0
    开始时：         mid,fast
    第一次                          mid         fast
    快慢指针初始都在第一个点，假设成都是左son，
        然后慢指针作为root，每次往后走一位
        快指针比慢指针多走一位，作为右son
        如上图所示
    另外，第一个if，说明右son不存在，比如最开始
         第二个if，说明找到左son，因为左son的next就是root
    """
    def sortedListToBST2(self, head):
        return self.helper2(head, tail = None)
        
    def helper2(self, head, tail):
        if head == tail:
            return None
        if head.next == tail:
            return TreeNode(head.val)
        mid = head
        fast = head
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            mid = mid.next
        node = TreeNode(mid.val)
        node.left = self.helper2(head, mid)
        node.right = self.helper2(mid.next, tail)
        return node

#[-10,-3,0,5,9]
so = Solution()

ln0 = ListNode(10)
ln1 = ListNode(-3)
ln2 = ListNode(0)
# ln3 = ListNode(5)
# ln4 = ListNode(9)

head = ln0

ln0.next = ln1
ln1.next = ln2
ln2.next = None

# ln3.next = ln4
# ln4.next = None
print(so.sortedListToBST(head))
print(so.sortedListToBST2(head))
