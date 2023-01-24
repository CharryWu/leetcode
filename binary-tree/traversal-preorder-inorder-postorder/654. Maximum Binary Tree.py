# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        前文 手把手刷二叉树总结篇 说过二叉树的递归算法可以分两类，一类是遍历二叉树的类型，一类是分解子问题的类型。
        前者较简单，只要运用二叉树的递归遍历框架即可；后者的关键在于明确递归函数的定义，然后利用这个定义。
        这题是后者，函数 build 的定义是根据输入的数组构造最大二叉树，那么只要我先要找到根节点，然后让 build 函数递归生成左右子树即可。
        """
        n = len(nums)
        def findMaxIdx(start, end):
            """
            找到左闭右开区间[start, end)中的最大值和对应的索引
            """
            if start == end: # base case
                return None
            elif start == end-1: # base case
                return start
            m = nums[start]
            res = start
            for i in range(start, end):
                if nums[i] > m:
                    m = nums[i]
                    start = i
            return start
        
        def build(start, end):
            """
            定义：将 nums[lo..hi] 构造成符合条件的树，返回根节点
            """
            if start == end: # base case
                return None
            elif start == end-1: # base case
                return TreeNode(val=nums[start])
            max_idx = findMaxIdx(start, end)
            left = build(start, max_idx) # 递归调用构造左右子树
            right = build(max_idx+1, end) # 递归调用构造左右子树
            cur = TreeNode(val=nums[max_idx], left=left, right=right)
            return cur
        
        return build(0, n)