# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """
        前文 手把手刷二叉树总结篇 说过二叉树的递归分为「遍历」和「分解问题」两种思维模式，这道题需要用到「遍历」的思维。
        BST 的中序遍历有序，在中序遍历的位置做一些判断逻辑和操作有序数组差不多，很容易找出众数。
        """
        res = []
        prev = None
        cur_count = 0 # 当前元素的重复次数
        max_count = 0 # 全局的最长相同序列长度
        
        def traverse(n):
            nonlocal cur_count
            nonlocal max_count
            nonlocal prev
            nonlocal res
            if not n:
                return
            traverse(n.left)
            
            # 中序遍历位置
            if not prev:
                cur_count, max_count = 1, 1
                res.append(n.val)
            else:
                if n.val == prev.val: # n.val 重复的情况
                    cur_count += 1
                    if cur_count == max_count: # n.val 是众数
                        res.append(n.val)
                    elif cur_count > max_count:
                        # 更新众数
                        res = [n.val] # 重置结果数组
                        max_count = cur_count

                if n.val != prev.val: # n.val 不重复的情况
                    cur_count = 1
                    if cur_count == max_count:
                        res.append(n.val)
                    
            prev = n # 别忘了更新 prev
            traverse(n.right)
        
        traverse(root)
        return res