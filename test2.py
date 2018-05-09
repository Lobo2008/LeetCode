

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
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        sum = flag1 = flag2 = 0
        while l1:
            sum += l1.val * 10 ** flag1
            flag1 += 1
            l1 = l1.next
        while l2:
            sum += l2.val * 10 ** flag2
            flag2 += 1
            l2 = l2.next
        h = m = ListNode(0) # h = 0
        if not sum: # if sum == 0
           return h
        if sum:#807  -> 708
           m.next = ListNode(res % 10) #fist: 7 then 0,last 8
           sum /= 10
           m = m.next
