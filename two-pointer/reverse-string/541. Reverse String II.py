class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ss = list(s)
        n = len(ss)
        
        cur = 0
        while cur < n:
            i, j = cur, min(cur+k-1, n-1)
            while i < j:
                ss[i], ss[j] = ss[j], ss[i]
                i += 1
                j -= 1
            cur += 2 * k
            
        
        return ''.join(ss)
