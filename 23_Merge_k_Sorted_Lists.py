"""

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6


"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        """
        list里有k个链表，最长的链表长度是n,每个链表取出第一个元素，得到k个元素，然后k个元素排序以后放入链表。
        每一次排序是klgk，最多需要取n次，所以是 n*k*lgk?
        Input:
        [
            1->4->5,
            1->3->4,
            2->6
        ]
        Output: 1->1->2->3->4->4->5->6

        记录当前结果栈中最大的元素就是栈顶

        遍历每个链表，如果连

        """
        print('--------in function------')
        if len(lists) == 0 : return None
        ls =[]
        for oneList in lists:
            while oneList:
                ls.append(oneList.val)
                oneList = oneList.next
        ls.sort()
        head = dumphead = ListNode(None)
        for one in ls:
            head.next = ListNode(one)
            head = head.next
        return dumphead.next



so = Solution()

lists = []
l11 = ListNode(1); l12 = ListNode(4); l13 = ListNode(5)
l1 = l11
l11.next = l12; l12.next = l13

l21 = ListNode(1); l22 = ListNode(3); l23 = ListNode(4)
l2 = l21
l21.next = l22; l22.next = l23

l31 =ListNode(2); l32 = ListNode(6)
l3 = l31
l31.next = l32
lists.extend([l1,l2,l3])


l4 = ListNode(None)

# lists = []
# lists.extend([l1,l4,l3])
# print(lists)
print('---input----')
for one in lists:
    while one:
        print(one.val)
        one = one.next


rs = so.mergeKLists(lists)
print('----rs-----')
while rs:
    print(rs.val)
    rs = rs.next


