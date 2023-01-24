# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        """
        硬币的移动规则看似很复杂，因为一个节点可能需要移出硬币，也可能移入硬币，还要求移动次数最少。实际上我们需要观察规律，做一些等价。
        如果一个节点的硬币个数是 x，无论是移出还是移入，把该节点的硬币个数变成 1 的最少移动次数必然是 abs(x - 1)。
        """
        res = 0
        def traverse(node):
            """
            定义：输入一棵二叉树，返回这棵二叉树中多出的硬币个数，返回负数代表缺少硬币
            """
            nonlocal res
            if not node:
                return 0
            
            left = traverse(node.left)
            right = traverse(node.right)
            # 让当前这棵树平衡所需的移动次数
            res += abs(left) + abs(right) + node.val - 1
            # 实现函数的定义
            return left+right+node.val-1 # 需要 node.val-1 次移动才能将node变成1
        traverse(root)
        return res