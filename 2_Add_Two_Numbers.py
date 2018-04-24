"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

How to build linkedlist 2 -> 4 -> 3 ->None using python

head = ListNode(2)
p1 = ListNode(4)
p2 = ListNode(3)
head.next = p1
p1.next = p2
p2.next = None

>>head.val
2
>>head.next.val
4
etc


"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = flag1 = flag2 = 0
        while l1:
            print (l1.val)
            sum += l1.val * 10 ** flag1 #   10**3 = 1000
            flag1 += 1
            l1 = l1.next #point to the next digit
        while l2:
            print (l2.val)
            sum += l2.val * 10 ** flag2
            flag2 += 1
            l2 = l2.next
        h = m = ListNode(0)
        if not sum:
            return h
        print ('sum=',sum)
        while sum:
            m.next = ListNode(sum % 10) 
            sum /= 10
            m = m.next
        return h.next 
head = ListNode(2)
p1 = ListNode(4)
p2 = ListNode(3)
head.next = p1
p1.next = p2
p2.next = None

nhead = ListNode(5)
np1 = ListNode(6)
np2 = ListNode(4)
nhead.next = np1
np1.next = np2
np2.next = None
res = Solution.addTwoNumbers(1,head,nhead)
