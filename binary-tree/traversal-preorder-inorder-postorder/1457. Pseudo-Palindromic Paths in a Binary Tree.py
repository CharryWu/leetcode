# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        """
        pseudo-palindromic path 中最多只能有一个节点出现次数为奇数
        The number of nodes in the tree is in the range [1, 105].
        1 <= Node.val <= 9
        """
        count = [0]*10
        res = 0
        def isPathPseudoPalindrome():
            odd_count = 0
            for c in count:
                if c % 2 == 1:
                    odd_count += 1
            return odd_count <= 1

        def traverse(node):
            nonlocal count
            nonlocal res
            if not node:
                return
            count[node.val] += 1
            if not node.left and not node.right and isPathPseudoPalindrome():
                res += 1
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            count[node.val] -= 1
        
        traverse(root)
        return res