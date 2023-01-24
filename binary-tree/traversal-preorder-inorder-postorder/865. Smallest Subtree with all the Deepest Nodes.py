from collections import deque
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """
        Intuition:
        My approach was to perform BFS and store only the first and last node at the deepest level.
        Find the LCA of first and last node.
        Thus it is ensured that all the other nodes between the first and last node will be part of the LCA found.
        
        Approach:
        We first use BFS, i.e., Level Order Traversal on the tree and find out the first and last nodes of the deepest level.
        Then we return their lca using the standard recursive procedure. Although, it is a two pass solution, it's really easy to understand how it works
        """
        queue = deque([root])
        first, last = None, None

        def lca(node, p, q):
            if not node or node == p or node == q:
                return node
            left = lca(node.left, p, q)
            right = lca(node.right, p, q)

            if left and right:
                return node
            if left:
                return left
            if right:
                return right
            return None
        
        while queue:
            first, last = queue[0], queue[-1]
            sz = len(queue)
            for i in range(sz):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return lca(root, first, last)
