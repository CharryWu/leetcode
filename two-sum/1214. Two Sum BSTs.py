# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        arr1, arr2 = [], []
        # 将两个 BST 转化成两个有序数组
        def dfs(n, arr):
            if not n:
                return
            dfs(n.left, arr)
            arr.append(n.val)
            dfs(n.right, arr)
        
        dfs(root1, arr1)
        dfs(root2, arr2)
        
        n1, n2 = len(arr1), len(arr2)
        # 对有序数组执行两数之和问题的算法逻辑
        # 这里也可以用二叉搜索法
        i1, i2 = 0, n2 - 1
        while i1 < n1 and i2 >= 0:
            s = arr1[i1] + arr2[i2]
            if s < target:
                # 让和大一些
                i1 += 1
            elif s > target:
                # 让和小一些
                i2 -= 1
            else:
                # 找到和 target
                return True
        return False
