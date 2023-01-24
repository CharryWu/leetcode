# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        res = []
        canflip = True
        cur_idx = 0
        def traverse(node):
            nonlocal canflip
            nonlocal cur_idx
            if not node or not canflip:
                return
            if node.val != voyage[cur_idx]: # 节点的 val 对不上，必然无解
                cur_idx += 1
                canflip = False
                return

            cur_idx += 1
            if node.left and node.left.val != voyage[cur_idx]:
                node.left, node.right = node.right, node.left
                res.append(node.val) # 记录翻转节点
            
            traverse(node.left)
            traverse(node.right)

        traverse(root) # 遍历的过程中尝试进行反转
        if canflip:
            return res
        return [-1]
            