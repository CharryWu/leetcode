# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        res = ""
        if not root:
            return ""
        
        ss, ds = [], []
        foundS, foundE = [], []

        def dfsStart(n):
            if not n:
                return False
            
            ss.append(n)
            if n.val == startValue:
                nonlocal foundS ##注意用nonlocal，否则foundS会被认为是local variable
                foundS = list(ss)
                ss.pop()
                return True
            if dfsStart(n.left) or dfsStart(n.right):
                ss.pop()
                return True
            ss.pop()
            return False
        
        
        def dfsEnd(n):
            if not n:
                return False
            
            ds.append(n)
            if n.val == destValue:
                nonlocal foundE ##注意用nonlocal，否则foundS会被认为是local variable
                foundE = list(ds)
                ds.pop()
                return True
            if dfsEnd(n.left) or dfsEnd(n.right):
                ds.pop()
                return True
            ds.pop()
            return False
        
        dfsStart(root)
        dfsEnd(root)
        
        si, ei = -1, -1 ##这里从-1开始算起，因为我们需要找最低公共祖先节点。如果从0开始，for循环结束时si ei 指向的就不是祖先，而是是祖先的下一层了
        for ns, nd in zip(foundS, foundE):
            if ns == nd:
                si += 1
                ei += 1
            else:
                break
        
        res = []
        
        while si < len(foundS) - 1: # 这里while 去掉到达公共节点的一跳
            res.append('U')
            si += 1
            
        while ei < len(foundE):
            if ei < len(foundE) - 1:
                if foundE[ei+1] == foundE[ei].left:
                    res.append('L')
                elif foundE[ei+1]  == foundE[ei].right:
                    res.append('R')
            ei += 1
        return ''.join(res)

