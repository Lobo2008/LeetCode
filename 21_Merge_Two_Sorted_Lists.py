"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


Input: 1->2->4, 1->3->4-5
Output: 1->1->2->3->4->4

ls = [1,1,2,3,4,4]
list转ListNode

先定义一个头
head = ListNode(None)
head.next = None

然后把这个“赋值给”另外一个链表
l3 = head
接着对这个链表操作
for item in ls:
    l3.next = ListNode(item)
    l3 = l3.next
最后结果是存在 head 里面的


归并排序

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        resHead = ListNode(None)
        resHead.next = None
        p = resHead #  此时p已经跟l1和l2一样是一个ListNode了 ！！！！！！！
        while l1 and l2:
            if l1.val < l2.val:                
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return resHead.next #返回头部

    """
    递归解法
    """
    def mergeTwoLists_Recursive(self,l1,l2):
        if l1==None and l2==None:
            return None
        if l1==None:
            return l2
        if l2==None:
            return l1
        if l1.val<=l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2

heada = ListNode(None)
heada.next = None
pa = heada
lsa = [1,2,4]
lsa = [1]
for item in lsa:
    pa.next = ListNode(item)
    pa = pa.next

headb = ListNode(None)
headb.next = None
pb = headb
lsb = [1,3,4,5]
lsb = [2]
for item in lsb:
    pb.next = ListNode(item)
    pb = pb.next

while headb:
    # print(headb.val)
    headb = headb.next


res = Solution.mergeTwoLists(1, heada, headb) 

while res:
    print(res.val)
    res = res.next



