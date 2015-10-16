# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def print_(self):
        current = self
        while current:
            print str(current.val)+"->",
            current = current.next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return l1 if l1 else l2
        if l1.val > l2.val:
            merged_cursor = merged_head = l2
            l2 = l2.next
        else:
            merged_cursor = merged_head = l1
            l1 = l1.next
        
        while l1 and l2:
            if l1.val > l2.val:
                merged_cursor.next = l2
                l2 = l2.next
            else:
                merged_cursor.next = l1
                l1 = l1.next
            merged_cursor = merged_cursor.next

        merged_cursor.next = l1 if l1 else l2
        return merged_head

node1=[
    ListNode(1),
    # ListNode(2.5),
    # ListNode(3),
    # ListNode(40),
    # ListNode(50)
]

node2=[
    ListNode(2),
    # ListNode(2),
    # ListNode(3),
    # ListNode(30),
    # ListNode(100)
]

for i in range(len(node1)-1):
    node1[i].next = node1[i+1]
for i in range(len(node2)-1):
    node2[i].next = node2[i+1]

merged = Solution().mergeTwoLists(node1[0], node2[0])
merged.print_()