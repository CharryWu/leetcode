"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def traverse(node1, node2): # 三叉树遍历框架
            if not node1 or not node2:
                return
            node1.next = node2 # 将传入的两个节点穿起来
            traverse(node1.left, node1.right) # 将传入的两个节点穿起来
            traverse(node2.left, node2.right)
            traverse(node1.right, node2.left) # 连接跨越父节点的两个子节点
        
        if not root:
            return None
        traverse(root.left, root.right) # 遍历「三叉树」，连接相邻节点
        return root