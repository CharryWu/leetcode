# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        看这题的难度是困难，但你别被吓住了，我们从简单的开始，如果以整棵树的根节点为坐标 (0, 0)，你如何打印出其他节点的坐标？

        很简单，写出如下代码遍历一遍二叉树即可：

        ```
        void traverse(TreeNode root, int row, int col) {
            if (root == null) {
                return;
            }
            print(row, col);
            traverse(root.left, row + 1, col - 1);
            traverse(root.right, row + 1, col + 1);
        }
        ```
        """
        nodes = []
        def traverse(node, row, col):
            if not node:
                return
            nodes.append((col, row, node.val))
            traverse(node.left, row+1, col-1)
            traverse(node.right, row+1, col+1)
        
        traverse(root, 0, 0)

        nodes.sort()
        res = []
        preCol = float('-inf')
        for curCol, curRow, curVal in nodes:
            if curCol != preCol:
                res.append([])
                preCol = curCol
            res[-1].append(curVal)
        return res
            