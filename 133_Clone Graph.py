import pdb
# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node is None:
            return None
        node_clone = UndirectedGraphNode(node.label)
        unexplored_label = [[node, node_clone]]
        explored_node = {node_clone.label: node_clone}
        while len(unexplored_label) > 0:
            # pdb.set_trace()
            (tmp_node, tmp_node_clone)= unexplored_label.pop()
            for neighbor in tmp_node.neighbors:

                if neighbor.label == tmp_node.label:
                    tmp_node_clone.neighbors.append(tmp_node_clone)
                else:
                    # neighbor_clone.neighbors.append(tmp_node_clone)
                    if not neighbor.label in explored_node:
                        neighbor_clone = UndirectedGraphNode(neighbor.label)
                        tmp_node_clone.neighbors.append(neighbor_clone)
                        unexplored_label.append([neighbor, neighbor_clone])
                        explored_node[neighbor_clone.label] = neighbor_clone
                    else:
                        neighbor_clone = explored_node[neighbor.label]
                        tmp_node_clone.neighbors.append(neighbor_clone)
        # pdb.set_trace()
        return node_clone

node_list = [
    UndirectedGraphNode(0),
    UndirectedGraphNode(1),
    UndirectedGraphNode(2),
    UndirectedGraphNode(3),
    UndirectedGraphNode(4),
]
node_list[0].neighbors=[node_list[3], node_list[1]]
node_list[1].neighbors=[node_list[2]]
node_list[2].neighbors=[node_list[3]]
node_list[3].neighbors=[node_list[4]]

node_clone = Solution().cloneGraph(node_list[0])
pdb.set_trace()