# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        """
        如何知道一个节点 x 是「错误」节点？
        需要要知道它的右子节点错误地指向同层右侧的一棵子树。
        那么如何让节点 x 知道自己错指了呢？
        可以稍微改一下二叉树的遍历框架，先遍历右子树后遍历左子树，同时记录已遍历的节点。这样 x 如果发现自己的右子节点已经被访问了，就说明 x 节点是「错误」的。
        """
        visited = set()
        def traverse(n):
            if not n:
                return None
            
            if n.right and n.right in visited: # 找到「无效节点」，删除整棵子树
                return None
            visited.add(n) # 记录已遍历的节点
            # 先遍历右子树后遍历左子树
            n.right = traverse(n.right)
            n.left = traverse(n.left)
            return n
        
        return traverse(root)