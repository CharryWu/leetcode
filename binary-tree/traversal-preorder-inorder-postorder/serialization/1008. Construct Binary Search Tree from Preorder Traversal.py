class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def build(start, end):
            """
            定义：将 preorder[start..end] 区间内的元素生成 BST，并返回根节点
            """
            if start > end:
                return None
            # 根据前序遍历的特点，根节点在第一位，后面接着左子树和右子树
            rootVal = preorder[start]
            root = TreeNode(rootVal)
            # 根据 BST 的特点，左子树都比根节点的值小，右子树都比根节点的值大
            # p 就是左右子树的分界点
            p = start + 1
            while p <= end and preorder[p] < rootVal:
                p += 1
            
            root.left = build(start+1, p-1)
            root.right = build(p, end)
            
            return root
        return build(0, len(preorder)-1)
