class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        用分治方法写出来的代码
        """
        if not root:
            return []
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        return left + right + [root.val]



#class Solution:
#    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#        res = []
#        """
#        用分治方式写出来的代码
#        """
#        def traverse(n):
#            if not n:
#                return
#            traverse(n.left)
#            traverse(n.right)
#            res.append(n.val)
#        
#        traverse(root)
#        return res
#
