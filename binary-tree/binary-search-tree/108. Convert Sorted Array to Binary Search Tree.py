class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(s, e):
            if s == e:
                return None
            mid = (s+e)//2
            root = TreeNode(nums[mid])
            root.left = build(s, mid)
            root.right = build(mid+1, e)
            return root
        
        n = len(nums)
        return build(0, n)