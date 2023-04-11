"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, source: 'Node') -> 'Node':
        if not source:
            return None
        adj_list = {}
        visited = [False] * 101

        def traverse(node):
            if visited[node.val]:
                return
            neighborvals = []
            for neighbor in node.neighbors:
                neighborvals.append(neighbor.val)
            adj_list[node.val] = neighborvals

            visited[node.val] = True
            for neighbor in node.neighbors:
                traverse(neighbor)


        traverse(source)
        node_list = [None] * 101
        for key in adj_list:
            node_list[key] = Node(key)

        for key, neighbors in adj_list.items():
            newneighbors = []
            for neighbor in neighbors:
                newneighbors.append(node_list[neighbor])
            node_list[key].neighbors = newneighbors

        return node_list[source.val]