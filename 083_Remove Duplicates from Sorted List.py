import pdb
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hash_map = {}
        current = head
        tail = None
        while current:
            if hash_map.get(current.val, False):
                tail.next = current.next
            else:
                hash_map[current.val] = True
                tail = current
            current = current.next
        return head

node_list = [
    ListNode(0),
    ListNode(0),
    ListNode(1)
]
node_list[0].next = node_list[1]
node_list[1].next = node_list[2]

head = Solution().deleteDuplicates(node_list[0])
pdb.set_trace()
