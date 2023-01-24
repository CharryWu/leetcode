# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
        首先我们列举一下一个节点可能存在的几种状态：
        该节点不在监控区域内，称为 uncover 状态；该节点在附近节点的监控范围内，称为 cover 状态；该节点自己装了摄像头，称为 set 状态。
        如何保证安装的摄像头数量尽可能少呢？显然就是要尽可能分散，让每个摄像头物尽其用。
        具体来说就是自底向上安装摄像头，在叶子节点的父节点上安装摄像头，然后每隔两层再安装（因为每个摄像头都可以管三层）。
        那么一个节点在什么情况下需要被安装摄像头呢？显然是当这个节点的子节点处于 uncover 的状态的时候必须安装摄像头，以便覆盖子节点。
        综上，我们需要利用后序位置自底向上遍历二叉树，同时要利用子节点的状态以及父节点的状态，判断当前节点是否需要安装摄像头。
        """
        res = 0
        EMPTY, NON_COVERED, COVERED, SET = -1, 0, 1, 2
        def setCamera(node, hasParent):
            """
            定义：输入以 root 为根的二叉树，以最优策略在这棵二叉树上放置摄像头，然后返回 root 节点的情况：
            返回 -1 代表 root 为空，返回 0 代表 root 未被 cover，
            返回 1 代表 root 已经被 cover，返回 2 代表 root 上放置了摄像头。
            """
            nonlocal res
            if not node:
                return EMPTY
            leftStatus = setCamera(node.left, True)
            rightStatus = setCamera(node.right, True)

            if leftStatus == EMPTY and rightStatus == EMPTY: # 当前节点是叶子节点
                if hasParent:
                    return NON_COVERED # 有父节点的话，让父节点来 cover 自己
                else:
                    res += 1 # 特殊case: 整棵树只有root一个节点，root是叶子但是没有父节点，自己 set 一个摄像头
                    return SET
            
            if leftStatus == NON_COVERED or rightStatus == NON_COVERED: # 左右子树存在没有被 cover 的
                res += 1 # 必须在当前节点 set 一个摄像头
                return SET

            if leftStatus == SET or rightStatus == SET: # 左右子树只要有一个 set 了摄像头
                return COVERED # 当前节点就已经是 cover 状态了
            
            # 剩下 left == 1 && right == 1 的情况, 即当前节点的左右子节点都被 cover
            if hasParent:
                return NON_COVERED # 如果有父节点的话，可以等父节点 cover 自己
            else:
                # 没有父节点，只能自己 set 一个摄像头
                res += 1
                return 2