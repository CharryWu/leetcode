# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        target_depth = -1
        res = None

        def traverse(node, depth, targetVal): # 二叉树遍历函数
            """
            就知道前序遍历也可以找到 u 的相邻节点：
            先找到 u 的层数 targetDepth，然后再次走到 targetDepth 时遇到的就是 u 的相邻节点。
            """
            nonlocal target_depth
            nonlocal res
            if not node:
                return
            if res: # 找到 res，不用再进行搜索了，立即停止
                return
            if targetVal == node.val: # 找到目标层数
                target_depth = depth
            elif depth == target_depth: # 找到下一个当前层数的节点，此时 node 一定是最靠近 u 的，立即返回停止搜索
                res = node
                return
        
            traverse(node.left, depth+1, targetVal)
            traverse(node.right, depth+1, targetVal)

        traverse(root, 0, u.val)
        return res 