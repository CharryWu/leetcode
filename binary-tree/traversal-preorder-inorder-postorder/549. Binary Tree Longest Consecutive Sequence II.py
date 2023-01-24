class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def longest_path(root: TreeNode) -> List[int]:
            nonlocal maxval
            
            if not root:
                return [0, 0]
            
            inr = dcr = 1
            if root.left:
                left = longest_path(root.left)
                if (root.val == root.left.val + 1):
                    dcr = left[1] + 1
                elif (root.val == root.left.val - 1):
                    inr = left[0] + 1
            
            if root.right:
                right = longest_path(root.right)
                if (root.val == root.right.val + 1):
                    dcr = max(dcr, right[1] + 1)
                elif (root.val == root.right.val - 1):
                    inr = max(inr, right[0] + 1)
                    
            maxval = max(maxval, dcr + inr - 1)
            return [inr, dcr]
        
        maxval = 0
        longest_path(root)
        return maxval


### My code doesn't work
# class Solution:
#     def longestConsecutive(self, root: Optional[TreeNode]) -> int:
#         res = 1
#         def traverse(n):
#             nonlocal res
#             lcount, rcount = 0, 0
#             lsign, rsign = 0, 0
#             total_count = 1
#             if n.left:
#                 lcount = traverse(n.left)
#                 if n.val == n.left.val + 1 or n.val == n.left.val - 1:
#                     lsign = n.val - n.left.val
#                     total_count = max(total_count, lcount+1)

#             if n.right:
#                 rcount = traverse(n.right)
#                 if n.val == n.right.val + 1 or n.val == n.right.val - 1:
#                     rsign = n.val - n.right.val
#                     total_count = max(total_count, rcount+1)

#             if lsign != 0 and lsign == -rsign:
#                 total_count = lcount + rcount + 1
#             res = max(res, total_count)
#             return total_count

#         traverse(root)
#         return res
