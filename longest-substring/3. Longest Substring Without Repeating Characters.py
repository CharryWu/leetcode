class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        freq = {}
        rep = set()
        
        def add(c):
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
                if freq[c] > 1:
                    rep.add(c)

        def remove(c):
            if c in freq:
                freq[c] -= 1
                if freq[c] <= 1 and c in rep:
                    rep.remove(c)
                    
        
        left, right = 0, 0
        n = len(s)
        res = 0
        while right < n:
            add(s[right])
            while len(rep) > 0:
                remove(s[left])
                left += 1
            res = max(right-left+1, res)
            right += 1
        
        return res
            
