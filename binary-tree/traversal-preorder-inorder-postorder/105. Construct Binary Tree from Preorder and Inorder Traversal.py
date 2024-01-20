# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        inorder 作用就是通过寻找 rootindex 得知左右子树的节点大小
        preorder 获取当前根节点
        """
        valToIndex = {} # 用反向索引装 val -> inorder index
        for i in range(len(inorder)):
            valToIndex[inorder[i]] = i
        def build(preorder, inorder, preStart, preEnd, inStart, inEnd) -> TreeNode:
            """
            Build a tree with preorder[preStart] as root value, and recursively
            build left & right subtree
            return the built root node
            """
            if preStart > preEnd:
                return None
            rootVal = preorder[preStart]
            rootIndex = valToIndex[rootVal]
            leftSize = rootIndex-inStart
            rightSize = inEnd - rootIndex
            root = TreeNode(rootVal)
            root.left = build(preorder, inorder, preStart + 1, preStart + leftSize, inStart, rootIndex-1)
            root.right = build(preorder, inorder, preStart + leftSize + 1, preEnd, rootIndex + 1, inEnd)
            return root
        return build(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)
