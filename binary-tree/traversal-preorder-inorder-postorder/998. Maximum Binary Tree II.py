# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        做这道题之前，你一定要去做一下 654. 最大二叉树 这道题，知道了构建最大二叉树的逻辑就很容易解决这道题了。
        新增的 val 是添加在原始数组的最后的，根据构建最大二叉树的逻辑，正常来说最后的这个值一定是在右子树的，可以对右子树递归调用 insertIntoMaxTree 插入进去。
        但是一种特殊情况是 val 比原始数组中的所有元素都大，那么根据构建最大二叉树的逻辑，原来的这棵树应该成为 val 节点的左子树。
        """
        def traverse(n, p):
            if not n:
                if not p.right:
                    p.right = TreeNode(val=val)
                    return True
                else:
                    return False
            
            if val > n.val:
                insert_node = TreeNode(val=val, left=n)
                if n == p.left:
                    p.left = insert_node
                else:
                    p.right = insert_node
                return True
            else:
                right_inserted = traverse(n.right, n)
                if right_inserted:
                    return True
            return False
        dummy = TreeNode(val=float('inf'), right=root)
        traverse(root, dummy)
        return dummy.right