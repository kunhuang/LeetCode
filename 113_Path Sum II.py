import pdb
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.sum = sum
        self.current_sum = 0
        self.path_stack = []
        self.result = []

        if root is None:
            return []

        self.dfs(root)
        return self.result

    def dfs(self, node):
        self.path_stack.append(node.val)
        self.current_sum += node.val
        # pdb.set_trace()
        if node.left is None and node.right is None:
            if self.current_sum == self.sum:
                self.result.append(self.path_stack[:])    
        else:
            if node.left:
                self.dfs(node.left)
            if node.right:
                self.dfs(node.right)
        self.path_stack.pop()
        self.current_sum -= node.val

node_list = [
    TreeNode(5),
    TreeNode(4),
    TreeNode(2),
    TreeNode(2),
    # TreeNode(13),
    # TreeNode(5),
    # TreeNode(6)
]

node_list[0].left = node_list[1]
node_list[0].right = node_list[2]
node_list[2].left = node_list[3]

print Solution().pathSum(node_list[0], 7)