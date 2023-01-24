class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if not p or not q:
            return None
        pp, qq = p, q
        while pp != qq:
            if pp.parent:
                pp = pp.parent
            else:
                pp = q
            
            if qq.parent:
                qq = qq.parent
            else:
                qq = p
            
        
        return pp