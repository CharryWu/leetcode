class Solution:
    def pathSum(self, nums: List[int]) -> int:
        """
        这题很有意思，需要综合好几个技巧。

        首先，你可以先看一下 113. 路径总和 II 这道题的思路，学习如何遍历得到所有二叉树的路径。

        然后，这道题还会用到 1104. 二叉树寻路 和 987. 二叉树的垂序遍历 中给完全二叉树编号的技巧。
        
        每个节点的前两位就是它的 code 编号

        这里我们无法用常规的 left, right 指针来遍历左右子节点，但是可以通过父节点的编号计算出子节点的编号，从而确定子节点。
        在这道题中，假设父节点在行中的编号为 x，则左子节点为下一行的 2 * x - 1，右子节点为下一行的 2 * x。
        """
        tree = {}
        pathsum = 0
        
        for code in nums:
            val = code % 10
            code = code // 10
            tree[code] = val
        
        # 输入已经排序，第一个就是根节点
        rootCode = nums[0] // 10
        
        # 将 (depth, id) 编码为十进制两位数
        def encode(depth, i):
            return 10 * depth + i
        
        # 二叉树遍历函数，顺便记录遍历过得路径之和
        def dfs(code, path):
            if code not in tree:
                return
            # 当前遍历到的节点值
            val = tree[code]
            # 当前遍历到的节点深度和 位置
            depth, i = code // 10, code % 10
            # 左右子节点的编码
            leftCode, rightCode = encode(depth + 1, i * 2 - 1), encode(depth + 1, i * 2)
            if leftCode not in tree and rightCode not in tree:
                nonlocal pathsum
                pathsum += (path + val)
                return
            # 二叉树遍历框架
            dfs(leftCode, path + val)
            dfs(rightCode, path + val)

        dfs(rootCode, 0)
        return pathsum
