# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        得益于二叉搜索树左小右大的特性，一个重要性质是：二叉搜索树的中序遍历结果有序。
        题目说有两个节点的值反了，也就是说中序遍历结果不再是有序的，有两个元素的位置反了。
        那么我们在中序遍历的时候找到破坏有序性的这两个元素，交换它们即可。
        这两个元素在中序遍历后的数组中一定是紧邻的，如果不是紧邻的，则会出现多个相反顺序，和题意不符
        """
        first, second = None, None # 分别记录这两个被交换的节点
        prev = TreeNode(val=float('-inf')) # 判断中序遍历的有序性

        def traverse(n):
            """
            中序遍历代码位置，找出那两个节点
            """
            nonlocal first
            nonlocal second
            nonlocal prev
            if not n:
                return
            traverse(n.left)
            if prev.val > n.val: # n 不符合有序性
                if not first:
                    first = prev # 第一个错位节点是 prev
                second = n
            prev = n
            traverse(n.right)
        
        traverse(root)
        first.val, second.val = second.val, first.val
