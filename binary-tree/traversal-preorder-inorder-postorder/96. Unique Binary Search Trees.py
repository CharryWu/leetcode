class Solution:
    def numTrees(self, n: int) -> int:
        """
        假设给算法输入 n = 5，也就是说用 {1,2,3,4,5} 这些数字去构造 BST。
        如果固定 3 作为根节点，左子树节点就是 {1,2} 的组合，右子树就是 {4,5} 的组合：
        那么 {1,2} 和 {4,5} 的组合有多少种呢？只要合理定义递归函数，这些可以交给递归函数去做。
        另外，这题存在重叠子问题，可以通过备忘录的方式消除冗余计算。
        """
        # 备忘录
        memo = [[0]*(n+1) for _ in range(n+1)] # 备忘录的值初始化为 0
        
        # 包含所有来自 [lo, hi] 区间的数子树构型数量
        def count(lo, hi):
            if lo > hi: # base case: 子树没有任何节点，此时返回1代表空子树只有一种构型
                return 1
            # 查备忘录
            if memo[lo][hi] > 0:
                return memo[lo][hi]
            res = 0
            for mid in range(lo, hi+1):
                left = count(lo, mid-1) # 左子搜索树构型的数量
                right = count(mid+1, hi) # 右子搜索树构型的数量
                res += (left*right) # 以mid为根节点的构型数量
            
            memo[lo][hi] = res # 将结果存入备忘录
            return res
    
        return count(1, n)
