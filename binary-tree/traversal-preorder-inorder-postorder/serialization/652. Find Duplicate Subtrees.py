# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        如果你想知道以自己为根的子树是不是重复的，是否应该被加入结果列表中，你需要知道什么信息？
        你需要知道以下两点：
        1、以我为根的这棵二叉树（子树）长啥样？
        2、以其他节点为根的子树都长啥样？
        
        这就叫知己知彼嘛，我得知道自己长啥样，还得知道别人长啥样，然后才能知道有没有人跟我重复，对不对？
        我怎么知道自己以我为根的二叉树长啥样？前文 序列化和反序列化二叉树 其实写过了，二叉树的前序/中序/后序遍历结果可以描述二叉树的结构。
        我咋知道其他子树长啥样？每个节点都把以自己为根的子树的样子存到一个外部的数据结构里即可。
        按照这个思路看代码就不难理解了。
        """
        memo = {} # 记录所有子树以及出现的次数
        res = [] # 记录重复的子树根节点
        
        def traverse(n):
            if not n:
                return '#'
            left = traverse(n.left) # left 是 str
            right = traverse(n.right) # right 是 str
            
            # 后序遍历构建二叉树的representation
            sub_tree = f'{left},{right},{str(n.val)}'
            
            freq = memo[sub_tree] if sub_tree in memo else 0
            if freq == 1: # 多次重复也只会被加入结果集一次
                res.append(n)
            # 给子树对应的出现次数加一
            memo[sub_tree] = freq + 1
            return sub_tree
        
        traverse(root)
        return res