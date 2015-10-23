# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.current_num = 0
        if root is None:
            return 0
        self.DFS(root)
        return self.sum

    def DFS(self, node):
        self.current_num = self.current_num*10+node.val
        if node.left:
            self.DFS(node.left)
        if node.right:
            self.DFS(node.right)
        if node.left is None and node.right is None:
            self.sum += self.current_num
        self.current_num = (self.current_num-node.val)/10

node = [
    TreeNode(1),
    TreeNode(2),
    TreeNode(3),
]
node[0].left = node[1]
node[0].right = node[2]

print Solution().sumNumbers(node[0])