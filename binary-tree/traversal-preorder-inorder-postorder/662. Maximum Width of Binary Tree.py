# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Using recursive dfs method, label each node using heap index (so that null node still occupies one position)
        Have a global hashmap storing level => (leftmost pos, rightmost pos)
        result is max(rightmost - leftmost) + 1, since the level width includes both leftmost node and rightmost node
        e.g.
        1  <-- root
        2 3  <-- second level
        4 5 6 7  <-- third level
        """
        levelinfo = {}
        res = float('-inf')

        def dfs(node, level, pos):
            nonlocal res, levelinfo
            if not node:
                return
            if level not in levelinfo:
                levelinfo[level] = [pos, pos]

            levelinfo[level][0] = min(levelinfo[level][0], pos)
            levelinfo[level][1] = max(levelinfo[level][1], pos)
            res = max(res, levelinfo[level][1]-levelinfo[level][0])

            dfs(node.left, level+1, pos*2+1)
            dfs(node.right, level+1, pos*2+2)
        dfs(root, 0, 0)
        return res+1
