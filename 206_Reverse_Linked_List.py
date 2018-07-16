"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        Input: 1->2->3->4->5->NULL
        Output: 5->4->3->2->1->NULL
        newH = 
        #方法1，利用指针，ref：https://leetcode.com/problems/reverse-linked-list/discuss/140916/Python-Iterative-and-Recursive

         1->2->3->4->5->None
         先构造 1->None
         然后当前的元素cur作为下一轮的前缀元素  pre = cur
         所以得到了 2->  1->None
        当cur=5时，pre = cur = 5,再一次的while循环就进不去了，此时链表头就是 pre的值，返回pre

        """
        pre = None
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
        return pre

    """ 
    方法2：递归法，

    """
    def reverseList_recurssive(self, head):
        pass

so = Solution()
p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)
head = p1

p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = None

print(so.reverseList(head))