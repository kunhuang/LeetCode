import pdb
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None or (root.left is None and root.right is None):
            return

        self.dfs(root)

    def dfs(self, node):
        if node.left and node.right:
            tmp_node = node.right
            node.right = node.left
            node.left = None
            self.dfs(node.right).right = tmp_node
            return self.dfs(tmp_node)
            
        elif node.right:
            return self.dfs(node.right)

        elif node.left:
            node.right = node.left
            node.left = None
            return self.dfs(node.right)

        return node

node_list = [
    TreeNode(1),
    TreeNode(2),
    TreeNode(3),
    TreeNode(4),
    TreeNode(5),
    # TreeNode(5),
    # TreeNode(6)
]

node_list[0].left = node_list[1]
node_list[0].right = node_list[4]
node_list[4].left = node_list[2]
# node_list[1].left = node_list[2]
# node_list[1].right = node_list[3]

Solution().flatten(node_list[0])
pdb.set_trace()