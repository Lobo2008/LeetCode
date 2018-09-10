"""
 Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space? 

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        判断链表是否有环，有的话，返回环的入口，没有则返回null
        首先，用快慢两个指针判断是否有环，刚开始的时候两个指针都指向链表头
        然后，快指针每次走两步，慢指针每次走一步，当快慢两指针相遇的时候，找到环
                <-------
               /       |
        1->2->3->4->5->6
        p  q
           p     q
              p        q
                 pq  已经追上 说明有环，下面就开始找环的入口
        -------------------------        
        s           p
            s         p
              sp 相等的时候就是环的入口      
        如果快指针指向了null，说明没有环，直接返回null
        """
        try:
            p = head
            q = head.next
            while p is not q:
                p = p.next
                q = q.next.next #只要是指向的none，就会到except，所以这里可以随便写
        except:
            return None
        #当pq相等的时候，说明有环，那现在就处理环的入口
        fast = p.next
        slow = head
        while slow is not fast:#因为有环，所以肯定能在相等的时候退出while
            fast = fast.next
            slow = slow.next
        #当fast=slow的时候，就是上面图中的sp点，这就是入口，直接返回其中一个就可以
        return fast


        # try:
        #     fast = head.next
        #     slow = head
        #     while fast is not slow:
        #         fast = fast.next.next
        #         slow = slow.next
        # except:
        #     # if there is an exception, we reach the end and there is no cycle
        #     return None

        # # since fast starts at head.next, we need to move slow one step forward
        # slow = slow.next
        # while head is not slow:
        #     head = head.next
        #     slow = slow.next

        # return head


        """无法解 head.next =  head的情况
        p = q = head
        count = 0
        hasCycle = False
        while p and q:
            count += 1
            if p.next and q.next:#都没有指向空指针才有意义
                p = p.next
                q = q.next
                if q.next:
                    q = q.next
                else :#如果快指针指向了空指针，说明没环，直接返回none
                    return None
                #为了避免只有一个节点的时候p=q总是成立，所以必须移动一次以后(p.next,q.next)的相等才有意义
                if p == q:
                    hasCycle = True
                    break
            else:
                return None
        if hasCycle:
            p = q = head
            while count > 0:
                q = q.next
                count -= 1
            while p != q:
                p = p.next
                q = q.next
                if p == q:
                    return p
        return None#head=None 会走这里 
        """       

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
l6.next = l3 #正常情况，有环，注释以后就无环

"""单个节点，无环
head = ListNode(1)
"""

"""单个节点形成的环
head = ListNode(1)
head.next = head
"""
rs = so.detectCycle(head)
# print(so.detectCycle(head))
times = 10
while rs and times > 0 :
    print(rs.val)
    rs = rs.next
    times -= 1