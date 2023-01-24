# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    cur1, cur2 = p, q
    def dfs(root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None and root2 != None:
            return False
        if root1 != None and root2 == None:
            return False
        if root1 and root2:
            if root1.val != root2.val:
                return False

        return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)

    return dfs(p, q)

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: # edge case: subRoot 可能为空
            return subRoot == None
        
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)