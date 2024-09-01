
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Use dfs to clone
        Need a mapping from newly created node to old node to set up neighbors during dfs
        """
        mapping = {} # old node => new node

        def dfs_clone(node):
            """
            clone node and all its neighbors and adding all neighbors to newnode.neighbors
            """
            if not node:
                return None
            if node in mapping: # if new node has been created, don't create again
                return mapping[node]
            newnode = Node(node.val)
            mapping[node] = newnode
            for n in node.neighbors:
                newnode.neighbors.append(dfs_clone(n))
            return newnode

        return dfs_clone(node)
