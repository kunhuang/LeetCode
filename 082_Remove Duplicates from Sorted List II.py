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
        if head is None or head.next is None:
            return head

        new_head = ListNode(None)
        start = new_head
        
        start.next = head
        current = head.next

        duplicated = False

        while current:
            # pdb.set_trace()
            if current.val == start.next.val:
                duplicated = True
            else:
                if duplicated:
                    start.next = current
                    duplicated = False
                else:
                    start = start.next
                    # start = current
            current = current.next

        if duplicated:
            start.next = None

        return new_head.next
# 0, 1, 1, 2

# start      None  0 
# current    1     2 3
# duplicated False F T 

node_list = [
    ListNode(0),
    ListNode(1),
    ListNode(1),
    ListNode(2),
]
node_list[0].next = node_list[1]
node_list[1].next = node_list[2]
node_list[2].next = node_list[3]

head = Solution().deleteDuplicates(node_list[0])
pdb.set_trace()
