from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        level = 1
        while queue:
            sz = len(queue)
            for i in range(sz):
                top = queue.popleft()
                if not top.left and not top.right:
                    return level
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            level += 1
        return level
