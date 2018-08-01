"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """
        Given linked list: 1->2->3->4->5, and n = 2.
        删除倒数第n个节点
        两个指针p和q，初始时，第一个指针指向开始 即p=head
                          第二个指针向前n步，（从head开始数1，往后n步），即 q = head.next[.next][n-1]


        """
        if not head:    return None
        rs = ListNode(None)
        rs.next = head
        cur = runner = rs
        for _ in range(n):
            runner = runner.next
        while runner.next is not None:
            cur = cur.next
            runner = runner.next
        cur.next = cur.next.next

        return rs.next



        

so = Solution()      
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

head = l1
l1.next = l2; l2.next = l3; l3.next = l4; l4.next = l5


n = 2
rs = so.removeNthFromEnd(head,n)

while rs:
    print(rs.val)
    rs = rs.next