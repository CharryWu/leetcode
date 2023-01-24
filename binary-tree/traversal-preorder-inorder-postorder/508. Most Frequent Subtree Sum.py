# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = Counter()
        max_freq = 0
        res = set()
        
        def traverse(n):
            nonlocal max_freq
            nonlocal res
            if not n:
                return 0
            leftsum = traverse(n.left)
            rightsum = traverse(n.right)

            cur_sum = leftsum + rightsum + n.val
            freq[cur_sum] += 1
            
            if freq[cur_sum] == max_freq:
                res.add(cur_sum)
            elif freq[cur_sum] > max_freq:
                max_freq = freq[cur_sum]
                res = set([cur_sum])
        
            return cur_sum
        
        traverse(root)
        
        return list(res)