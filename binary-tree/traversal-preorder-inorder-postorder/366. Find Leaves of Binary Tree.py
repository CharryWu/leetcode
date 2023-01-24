# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        而这题可以需要思考，把二叉树的高度理解成从叶子节点到根节点从下到上递增的，那么把相同高度的节点分到一起就是题目想要的答案。
        那么，如何知道一个节点距离叶子节点的高度呢？
        首先，我们需要实现一个函数 maxDepth 计算这棵二叉树的最大高度；然后，我们在 maxDepth 函数的后序遍历位置就可以获取当前节点距离叶子节点的高度。
        """
        res = []
        
        # 定义：输入节点 root，返回以 root 为根的树的最大深度
        def dfs(n):
            if not n:
                return 0
            
            # 当前节点距离叶子节点的高度（最大深度）
            h = max(dfs(n.left), dfs(n.right)) + 1
            
            if len(res) < h: # 后序遍历位置
                res.append([])

            # 把所有相同高度的叶子节点放在一起
            res[h-1].append(n.val)
            return h
        
        dfs(root)
        return res
