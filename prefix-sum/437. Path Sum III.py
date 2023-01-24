from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        pathsum = 0
        presumcount = defaultdict(int)
        presumcount[0] = 1
        
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
            res += presumcount[pathsum-targetSum] # 当pathsum-targetSum不存在，res 不变(+=0)
            # 记录从二叉树的根节点开始，路径和为 pathSum 的路径条数
            presumcount[pathsum] = presumcount[pathsum] + 1
            
            dfs(n.left)
            dfs(n.right)
            
            # 后序遍历位置
            presumcount[pathsum] -= 1
            pathsum -= n.val
        
        dfs(root)
        return res
