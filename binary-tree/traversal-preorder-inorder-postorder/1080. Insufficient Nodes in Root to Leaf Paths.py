# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def isSufficient(n, s, p, isLeft):
            nonlocal limit
            s += n.val
            # 首先，对于一个叶子节点，它本身就是以自己为根的这棵二叉树的路径，
            # 那么这条路径是否小于 limit 的约束是很显然的，如果小于 limit，说明它需要被删除。
            if not n.left and not n.right:
                if s < limit:
                    if isLeft:
                        p.left = None
                    else:
                        p.right = None
                    return None, False
                else:
                    # return True
                    return n, True
            sufficient = False # 注意这里要初始化成false，只要有一条经过n 的path是sufficient的，n 就是sufficient的
            if n.left:
                lroot, lsufficient = isSufficient(n.left, s, n, True)
                sufficient = sufficient or lsufficient # 注意这里要用 or 操作符
            if n.right:
                rroot, rsufficient = isSufficient(n.right, s, n, False)
                sufficient = sufficient or rsufficient

            # 在后序去掉当前节点
            if not sufficient:
                if isLeft:
                    p.left = None
                else:
                    p.right = None
                return None, False
            return n, sufficient
        
        dummy = TreeNode(left=root)
        new_root, sufficient = isSufficient(root, 0, dummy, True)
        return dummy.left
