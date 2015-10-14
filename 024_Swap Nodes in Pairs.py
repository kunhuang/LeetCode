import pdb
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        cursor = head
        if head.next:
            head = head.next
        tail = None
        while cursor and cursor.next:
            if tail:
                tail.next = cursor.next
            tmp = cursor.next.next
            cursor.next.next = cursor
            cursor.next = tmp
            tail = cursor
            cursor = tmp
        return head


node=[
    ListNode(1),
    ListNode(2),
    ListNode(3),
    ListNode(4),
    ListNode(5),
    ListNode(6),
]
for i in range(len(node)-1):
    node[i].next = node[i+1]

def print_list(head):
    while head.next:
        print head.val, "->", 
        head = head.next
    print head.val

print_list(node[0])
head = Solution().swapPairs(node[0])
print_list(head)