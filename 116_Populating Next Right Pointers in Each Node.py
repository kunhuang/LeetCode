import pdb
# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root is None or root.left is None:
            return 
        self.recursive_scan(root)
        
    def recursive_scan(self, node):
        first_child = node.left
        if first_child is not None:
            while node.next:
                node.left.next = node.right
                node.right.next = node.next.left
                node = node.next
            node.left.next = node.right
            self.recursive_scan(first_child)

node_list = [
    TreeLinkNode(1),
    TreeLinkNode(2),
    TreeLinkNode(3),
    TreeLinkNode(4),
    TreeLinkNode(5),
    TreeLinkNode(6),
    TreeLinkNode(7)
]

node_list[0].left = node_list[1]
node_list[0].right = node_list[2]
node_list[1].left = node_list[3]
node_list[1].right = node_list[4]
node_list[2].left = node_list[5]
node_list[2].right = node_list[6]
# node_list[4].left = node_list[2]
# node_list[1].left = node_list[2]
# node_list[1].right = node_list[3]

Solution().connect(node_list[0])
pdb.set_trace()