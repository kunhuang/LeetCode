import pdb
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        current = head
        current_next = current.next
        current.next = None
        while current_next:
            # pdb.set_trace()
            tmp = current_next.next
            current_next.next = current
            current = current_next
            current_next = tmp

        return current

node_list = [
    ListNode(0),
    ListNode(1),
    ListNode(2)
]
node_list[0].next = node_list[1]
node_list[1].next = node_list[2]

head = Solution().reverseList(node_list[0])
pdb.set_trace()
