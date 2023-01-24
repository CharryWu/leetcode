class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        n = len(s)
        s = s[::-1]
        wp, cp = 0, 0
        
        while wp < n:
            if s[wp] == ' ':
                wp += 1
                continue
            
            cp = wp
            while cp < n and s[cp] != ' ':
                cp += 1
            nxt = cp
            tmp_str = ''
            while cp > wp:
                cp -= 1
                tmp_str += s[cp]
            res.append(tmp_str)
            res.append(' ')
            wp = nxt
            
        if res[-1] == ' ':
            res.pop()
        return ''.join(res)