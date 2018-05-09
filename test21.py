class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



b0 = ListNode(1)
b1 = ListNode(3)
b2 = ListNode(4)
b3 = ListNode(6)

b0.next = b1
b1.next = b2
b2.next = b3
b3.next = None

cx = ListNode(None)

bx = b0



ls = [1, 1, 2, 3, 4, 4, 6]

ln = ListNode(None)
ln.next = None
p = ln
for item in ls:
    print (item)
    p.next = ListNode(item)
    p = p.next

print("----")

while ln:
    print(ln.val)
    ln = ln.next
#"""
# arr1 = [1,2,3]

# l1 = ListNode(arr1[0])
# p1 = l1

# for i in arr1[1:]:
#     p1.next = ListNode(i)
#     p1 = p1.next
   

# print("----")
# print(p1.val)
# print(p1.next.val)
# print(p1.next.next.val)