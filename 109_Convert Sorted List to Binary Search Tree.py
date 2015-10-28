import pdb
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.length = 0
        self.current_cursor = head
        node = head

        while node:
            self.length += 1
            node = node.next

        if self.length == 0:
            return None
        if self.length == 1:
            return TreeNode(head.val)

        root = TreeNode(None)
        self.in_order(root, 0)
        return root

    def in_order(self, node, order):
        if 2*order+1 > self.length-1:
            node.val = self.current_cursor.val
            self.current_cursor = self.current_cursor.next
        
        elif 2*order+1 == self.length-1:
            left_node = TreeNode(self.current_cursor.val)
            node.left = left_node
            self.current_cursor = self.current_cursor.next
            node.val = self.current_cursor.val
            self.current_cursor = self.current_cursor.next
        
        else:
            left_node = TreeNode(None)
            node.left = left_node
            self.in_order(left_node, 2*order+1)
            
            node.val = self.current_cursor.val
            self.current_cursor = self.current_cursor.next

            right_node = TreeNode(None)
            node.right = right_node
            self.in_order(right_node, 2*order+2)
            

node_list = [
    ListNode(0),
    ListNode(1),
    ListNode(2),
    ListNode(3),
    ListNode(4),
    ListNode(5),
]
node_list[0].next = node_list[1]
node_list[1].next = node_list[2]
node_list[2].next = node_list[3]
node_list[3].next = node_list[4]
node_list[4].next = node_list[5]

root = Solution().sortedListToBST(node_list[0])
pdb.set_trace()