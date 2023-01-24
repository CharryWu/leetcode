# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        left_bound = []
        leaves = []
        right_bound = []

        leftcur = root.left
        while leftcur:
            if leftcur.left:
                left_bound.append(leftcur.val)
                leftcur = leftcur.left
            elif leftcur.right:
                left_bound.append(leftcur.val)
                leftcur = leftcur.right
            else: # found leave
                break

        def findLeaves(node):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
            findLeaves(node.left)
            findLeaves(node.right)
        findLeaves(root)

        
        rightcur = root.right
        while rightcur:
            if rightcur.right:
                right_bound.append(rightcur.val)
                rightcur = rightcur.right
            elif rightcur.left:
                right_bound.append(rightcur.val)
                rightcur = rightcur.left
            else:
                break

        return [root.val] + left_bound + leaves + right_bound[::-1]