class Solution:
    def isOneEditDistance(self, s: 'str', t: 'str') -> 'bool':
        """
        注意，这题问的是s, t两个字符串是否刚好是一个字符串的不同
        如果 s 和 t 完全相同，依然返回 False
        """
        ns, nt = len(s), len(t)

        if ns > nt:
            return self.isOneEditDistance(t, s)
        
        if nt-ns > 1:
            return False
        
        for i in range(ns):
            if s[i] != t[i]:
                if ns == nt:
                    return s[i+1:] == t[i+1:]
                else: # nt == ns+1
                    return s[i:] == t[i+1:]
        
        # postcond: all characters up until ns. s[0:ns] == t[0:ns]. nt could be the one additional characters
        # that makes edit distance exactly one between s and t
        return nt == ns+1