from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque([root])
        while len(queue):
            n = len(queue)
            for i in range(n): # 这里不能用 range(n-1)，要把当前level的所有节点都从 queue 里面 pop干净
                top = queue.popleft()
                if i < n-1:
                    top.next = queue[0]
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
        return root
