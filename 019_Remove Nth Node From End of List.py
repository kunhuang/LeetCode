import pdb
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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        n_ahead, current = head, head
        for i in range(n):
            current = current.next
        if current is None:
            return n_ahead.next
        while current.next:
            current = current.next
            n_ahead = n_ahead.next
        n_ahead.next = n_ahead.next.next
        return head

node=[
    ListNode(1),
    ListNode(2),
    ListNode(3),
    ListNode(4),
    ListNode(5)
]
for i in range(4):
    node[i].next = node[i+1]

root = Solution().removeNthFromEnd(node[0], 2)
root.print_()