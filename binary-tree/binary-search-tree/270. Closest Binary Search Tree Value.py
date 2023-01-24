# 分解思路：divide and conquer
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        if not root:
            return float('inf')
        
        if not root.left and not root.right:
            return root.val # base case: leave node
        
        if target == root.val:
            return root.val # found
        elif target < root.val:
            left = self.closestValue(root.left, target)
            if abs(target-left) < abs(target-root.val):
                return left
        elif target > root.val:
            right = self.closestValue(root.right, target)
            if abs(target-right) < abs(target-root.val):
                return right
        
        return root.val

# 遍历思路：traversal
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val
        
        def dfs(n):
            nonlocal res
            if not n:
                return
            curval = n.val
            if abs(curval - target) < abs(res - target):
                res = curval
            if curval == target:
                return
            elif target < n.val:
                dfs(n.left)
            else:
                dfs(n.right)

        dfs(root)
        return res
