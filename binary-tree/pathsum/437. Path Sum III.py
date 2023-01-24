from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        pathsum = 0
        seen = defaultdict(int)
        seen[0] = 1  # 注意别忘了设置 seen[0] = 1。如果path是从 root 开始，在root前 pathsum 就为0
        
        # 用回溯(前序+后序) + prefix sum 来解决问题
        def dfs(n):
            if not n:
                return
            # 前序遍历位置
            nonlocal pathsum
            nonlocal res
            pathsum += n.val
            # 从二叉树的根节点开始，路径和为 pathSum - targetSum 的路径条数
            # 就是路径和为 targetSum 的路径条数
            res += seen[pathsum-targetSum] # 当pathsum-targetSum不存在，res 不变(+=0)
            # 记录从二叉树的根节点开始，路径和为 pathSum 的路径条数
            seen[pathsum] += 1
            
            dfs(n.left)
            dfs(n.right)
            
            # 后序遍历位置
            seen[pathsum] -= 1 # 注意回溯的时候，seen 的状态也要回滚
            pathsum -= n.val # 回溯时，这两个statement顺序不能搞错。不然pathsum 作为 seen的索引不正确
        
        dfs(root)
        return res
