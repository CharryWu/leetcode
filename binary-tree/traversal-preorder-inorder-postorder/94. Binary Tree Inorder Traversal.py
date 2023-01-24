class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = []
        res = []
        
        def pushAllLeft(node, stack):
            while node:
                stack.append(node)
                node = node.left
        pushAllLeft(root, stack)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            pushAllLeft(cur.right, stack)
        return res
    
