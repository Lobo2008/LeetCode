"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


        res = ListNode(None)
        res.next = None
        p = res
        ls = []
        while head:
            if  head.val not in ls:
                ls.append(head.val)
                p.next = ListNode(head.val)
                p = p.next
            head = head.next
        return res.next

    """
    a better solution
    """
    def deleteDuplicates_2(self,head):
        p=head
        while p:
            while p.next and p.val==p.next.val:
                p.next=p.next.next
            p=p.next
        return head
ls = [1, 1, 2, 3, 3]
# ls = [1,1,2]
# ls = []
# ls = [0,0,0,0,0]
head = ListNode(ls[0])
head.next = None

p = head

for item in ls:
    p.next = ListNode(item)
    p = p.next

so = Solution()
res = so.deleteDuplicates(head)

while res:
    print('rs:',res.val)
    res = res.next

