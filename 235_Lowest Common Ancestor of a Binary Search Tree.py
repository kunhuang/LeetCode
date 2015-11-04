# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node = root
        if p.val > q.val:
            p, q = q, p

        while True:
            if node.val > q.val:
                node = node.left
            elif node.val < p.val:
                node = node.right
            else:
                return node

node_list = [
    TreeNode(2),
    TreeNode(3),
    TreeNode(0),
    TreeNode(0),
    TreeNode(0),
]    
node_list[0].right = node_list[1]
# node_list[0].right = node_list[2]
# node_list[1].left = node_list[3]
# node_list[1].right = node_list[4]

print Solution().lowestCommonAncestor(node_list[0], node_list[0], node_list[1]).val

