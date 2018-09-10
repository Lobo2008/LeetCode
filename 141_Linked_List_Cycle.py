"""
 Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?


"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            p = head
            q = head.next
            while p is not q:#有环的话，p 就会等于q，无环的话，会指向none，所以肯定会退出
                p = p.next
                q = q.next.next
            return True

        except:
            return False



so = Solution()
"""
                <-------
               /       |
        1->2->3->4->5->6

"""
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)



head = l1

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
# l6.next = l3 #正常情况，有环，注释以后就无环

"""单个节点，无环
head = ListNode(1)
"""

"""单个节点形成的环
head = ListNode(1)
head.next = head
"""
print(so.hasCycle(head))
