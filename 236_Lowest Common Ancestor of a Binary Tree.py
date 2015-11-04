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
        self.p = p
        self.q = q
        if id(root) == id(p) or id(root) == id(q):
            return root

        return self.dfs(root)

    def dfs(self, node):
        if node is None:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if isinstance(left, TreeNode):
            return left
        if isinstance(right, TreeNode):
            return right
        if id(node) == id(self.p):
            if left == 2 or right == 2:
                return node
            return 1 # means has p
        if id(node) == id(self.q):
            if left == 1 or right == 1:
                return node
            return 2 # means has q
        if left + right == 3:
            return node
        if left:
            return left
        if right:
            return right
        return 0

node_list = [
    TreeNode(0),
    TreeNode(0),
    TreeNode(0),
    TreeNode(0),
    TreeNode(0),
]    
node_list[0].left = node_list[1]
node_list[0].right = node_list[2]
node_list[1].left = node_list[3]
node_list[1].right = node_list[4]

print Solution().lowestCommonAncestor(node_list[0], node_list[3], node_list[2]).val



