# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None

        stack = [] # 用栈模拟递归建树过程
        i = 0
        
        while i < len(s):
            if s[i] == '(':
                i += 1
                continue
            if s[i] == ')': # 每次遇到有）括号，都说明栈顶节点构建完成
                i += 1
                stack.pop()
                continue

            ## 开始读取数字
            j = i
            num, sign = 0, 1
            if s[j] == '-':
                sign = -1
                j += 1
            
            while j < len(s) and '0' <= s[j] <= '9':
                num = num * 10 + ord(s[j])-ord('0')
                j += 1
            
            i = j-1
            num = num*sign
            ## 数字读取完成
            
            # 新建节点
            node = TreeNode(num)
            if stack:
                parent = stack[-1] # 栈顶元素永远是当前处理节点的父节点
                # 根据父节点的左右子节点情况组装
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
            stack.append(node)
            i += 1
        ### END WHILE LOOP
        
        # 注意到除了整棵树的根节点之外，
        # 其他的每个节点都可以找到一个有括号配对，
        # 所以最后栈中一定还有一个节点，就是根节点
        return stack[-1]